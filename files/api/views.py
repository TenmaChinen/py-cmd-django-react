from django.http import JsonResponse

def foo(request):
	l_foos = [ f'Foo {idx:02d}' for idx in range(1,5)]
	d_context = {
		'fooItemArray' : l_foos
	}
	return JsonResponse(d_context)