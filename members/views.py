from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
    try:
        mymember = Member.objects.get(id=id)
        template = loader.get_template('details.html')
        context = {
            'mymember': mymember,
        }
        return HttpResponse(template.render(context, request))
    except Member.DoesNotExist:
        return HttpResponse("Member not found.")
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
def testing(request):

    mymembers = Member.objects.all().order_by('first_name','id').values()
    template = loader.get_template('testing.html')
    context = {
       'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
def user_name(request):
    template = loader.get_template('user_name.html')
    context = {
        'user_name': 'Max Mustermann',
        'second_name': 'Max',
    }
    return HttpResponse(template.render(context, request))
