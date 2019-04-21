from django.shortcuts import render
from django.http import HttpResponse
import json

def fizzbuzz(request):
    if request.method == 'GET':
        params = request.GET
        try:
            start = int(params['begin']) if 'begin' in params else None
            end = int(params['end']) if 'end' in params else None
            if start is not None and end is not None:
                if start > end:
                    return HttpResponse('"begin" value must be less than or equal to "end" value.', status=422)
                resp = {}
                for i in range(start, end+1):
                    val = ''
                    if i % 3 == 0:
                        if i % 5 == 0:
                            val = 'fizzbuzz'
                        else:
                            val = 'fizz'
                    elif i % 5 == 0:
                        val = 'buzz'
                    resp[i] = val
                return HttpResponse(json.dumps(resp), status=200)     
            else:
                resp = []
                if start is None:
                    resp.append('Invalid "begin" value.')
                if end is None:
                    resp.append('Invalid "end" value.')                    
                return HttpResponse(resp.join('\n'), status=422)
        except:
            return HttpResponse('Valid parameters are "begin" and "end", both be integer values', status=422)
    else:
        # return 405 if they something other than a GET
        return HttpResponse(status=405)