from django.http import (
    HttpResponse, HttpResponseRedirect, JsonResponse,
    HttpResponseBadRequest, HttpResponseNotFound,
    HttpResponseForbidden, HttpResponseServerError,
    StreamingHttpResponse, FileResponse
)
from django.shortcuts import redirect
import os

def http_response_example(request):
    return HttpResponse("This is a basic HttpResponse example.")

def http_response_redirect(request):
    return HttpResponseRedirect("/response/http/")

def http_response_bad_request(request):
    return HttpResponseBadRequest("400 Bad Request")

def http_response_not_found(request):
    return HttpResponseNotFound("404 Not Found")

def http_response_forbidden(request):
    return HttpResponseForbidden("403 Forbidden")

def http_response_server_error(request):
    return HttpResponseServerError("500 Server Error")

def json_response_example(request):
    data = {"message": "This is a JSON response", "status": "success"}
    return JsonResponse(data)

def streaming_http_response_example(request):
    def stream_generator():
        for i in range(5):
            yield f"Chunk {i}\n"
    return StreamingHttpResponse(stream_generator(), content_type="text/plain")

def file_response_example(request):
    file_path = "path/to/your/example.txt"  # Replace with the actual file path
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename="example.txt")
    return HttpResponseNotFound("File not found")

def http_response_custom_graph(request):
    import matplotlib.pyplot as plt
    from io import BytesIO

    # Create a graph
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
    ax.set_title("Example Graph")

    # Save graph to in-memory file
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return HttpResponse(buf, content_type="image/png")
