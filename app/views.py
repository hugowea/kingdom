from django.shortcuts import render, HttpResponseRedirect
from .forms import SubordinateForm, KingForm
from .models import Question, Kingdom, King, Subordinate, Answer, Accept

def index(request):
    print("I am here")
    return render(request, 'app/index.html')

def subordinate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubordinateForm(request.POST)
        if form.is_valid():
            form.save()
            acc = Accept(subordinate=Subordinate.objects.get(name = request.POST['name']), king=King.objects.get(kingdom=request.POST['kingdom']), accepted = False)
            acc.save()        
        # check whether it's valid:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        return HttpResponseRedirect(f"/test_of_kingdom/{request.POST['kingdom']}/{request.POST['name']}/")

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {'form': SubordinateForm()}
        return render(request, 'app/subordinate.html', context)

def king(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        king = request.POST['name']

        kingdom = King.objects.get(pk = king).kingdom
        king_name = King.objects.get(pk = king).name
        kingdom_id = Kingdom.objects.get(kingdom_name = kingdom).pk
        
        subordinates = Subordinate.objects.filter(kingdom = kingdom_id)
        subordinates_accepted = Accept.objects.filter(king = King.objects.get(name = king_name), accepted = True)
        subordinates_accepted_new = [subordinate.subordinate for subordinate in subordinates_accepted]
        subordinates_accepted_names = [subordinate_accepted.subordinate.name for subordinate_accepted in subordinates_accepted]
        subordinates_new = [subordinate for subordinate in subordinates if subordinate.name not in subordinates_accepted_names]
        # print(request.POST)

        # check whether it's valid:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        return render(request, 'app/king_subordinates.html', context = {'subordinates': subordinates_new, 'subordinates_accepted': subordinates_accepted_new, 'king_name': king_name})
    else: 
        context = {'form': KingForm()}
        return render(request, 'app/king.html', context)

def king_subordinates(request, king_name):
    kingdom = King.objects.get(name = king_name).kingdom
    subordinates = Subordinate.objects.filter(kingdom = kingdom)
    subordinates_accepted = Accept.objects.filter(king = King.objects.get(name = king_name), accepted = True)
    subordinates_accepted_new = [subordinate.subordinate for subordinate in subordinates_accepted]
    subordinates_accepted_names = [subordinate_accepted.subordinate.name for subordinate_accepted in subordinates_accepted]
    subordinates_new = [subordinate for subordinate in subordinates if subordinate.name not in subordinates_accepted_names]
    # print(request.POST)

    # check whether it's valid:
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
    return render(request, 'app/king_subordinates.html', context = {'subordinates': subordinates_new, 'subordinates_accepted': subordinates_accepted_new, 'king_name': king_name})
    return render(request, 'app/king_subordinates.html', context = {'king_name': king_name})

def answer(request):
    return render(request, 'app/answer.html')

def results(request):
    return render(request, 'app/results.html')

def test_of_kingdom(request, kingdom_id, user_name):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print(request.POST)
        print(request.POST.dict())
        subordinate = Subordinate.objects.get(name = user_name)
        print(subordinate)
        dictionary = request.POST.dict()
        first_key = next(iter(dictionary))
        dictionary.pop(first_key)
        total_correct_answers = 0
        for key in dictionary:
            print(key)
            question = Question.objects.get(content=key)
            correct_answer = question.correct_answer
            isAnswerCorrect = False
            if dictionary[key] == correct_answer:
                isAnswerCorrect = True
                total_correct_answers += 1
            print(subordinate.pk)
            ans = Answer(subordinate=subordinate, question=question, isAnswerCorrect=isAnswerCorrect)
            ans.save()

        # check whether it's valid:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        result = total_correct_answers/len(dictionary)*100
        return render(request, 'app/results.html', context= {'result': result})
    else:
        kingdomName = Kingdom.objects.get(pk=kingdom_id)
        questions = Question.objects.filter(kingdom = kingdomName)
        return render(request, 'app/test.html', context={'questions': questions, 'kingdom_id': int(kingdom_id), 'user_name': str(user_name)})

def king_subordinate_result(request, king_name, subordinate_name):
    answers = Answer.objects.filter(subordinate=Subordinate.objects.get(name = subordinate_name))
    results = []
    sum_ball = 0
    for answer in answers:
        question = answer.question.content
        correct_answer = answer.question.correct_answer
        isAnswerCorrect = "верно" if answer.isAnswerCorrect else "неверно"
        ball = 1 if answer.isAnswerCorrect else 0
        sum_ball += ball
        results.append({'question': question, 'correct_answer': correct_answer, 'isAnswerCorrect': isAnswerCorrect, 'ball': ball})
    
    percent = sum_ball/len(answers)*100 if len(answers) != 0 else 0
    return render(request, 'app/king_subordinate_result.html', context={'subordinate_name': subordinate_name, 'results': results, 'sum_ball': sum_ball, 'percent': percent, 'king_name': king_name})

def king_subordinate_accept(request, king_name, subordinate_name):
    subordinate = Subordinate.objects.get(name = subordinate_name)
    acc = Accept.objects.get(subordinate= subordinate)
    acc.accepted = True
    acc.save()
    
    kingdom = King.objects.get(name = king_name).kingdom
    
    kingdom_id = Kingdom.objects.get(kingdom_name = kingdom).pk
    subordinates = Subordinate.objects.filter(kingdom = kingdom_id)
    
    subordinates_accepted = Accept.objects.filter(king = King.objects.get(name = king_name), accepted = True)
    subordinates_accepted_new = [subordinate.subordinate for subordinate in subordinates_accepted]
    subordinates_accepted_names = [subordinate_accepted.subordinate.name for subordinate_accepted in subordinates_accepted]
    subordinates_new = [subordinate for subordinate in subordinates if subordinate.name not in subordinates_accepted_names]
        # print(request.POST)

        # check whether it's valid:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
    return render(request, 'app/king_subordinates.html', context = {'subordinate_name': subordinate_name, 'subordinates': subordinates_new, 'subordinates_accepted': subordinates_accepted_new, 'king_name': king_name})
    

