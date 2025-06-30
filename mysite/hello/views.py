from django.http import HttpResponse

def my_view(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    
    resp = HttpResponse(f'view count={num_visits}')
    resp.set_cookie('dj4e_cookie', '6dee7f5a', max_age=1000)
    return resp 