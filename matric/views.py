from django.shortcuts import render, get_object_or_404
from .models import SchoolRecord
from .forms import SchoolRecordForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def matric_list(request):
	school_records = SchoolRecord.objects.all()
	return render(request, 'matric/matric_list.html', {'school_records': school_records})
   
   
def matric_detail(request, pk):
	school_record = get_object_or_404(SchoolRecord, pk=pk)
	return render(request, 'matric/matric_detail.html', {'school_record': school_record})   
	
@csrf_exempt	
def school_record_new(request):
	if request.method == "POST":
		form = SchoolRecordForm(request.POST)
		if form.is_valid():
			school_record = form.save(commit=False)
			#post.name = 'smotn'
			school_record.save()
			return redirect('matric_detail', pk=school_record.pk)
		#else:
		#	return HttpResponse(str(request.body) + '<h1>form not valid</h1>')
	else:
		form = SchoolRecordForm()
	return render(request, 'matric/matric_edit.html', {'form': form})	
	