from django.shortcuts import render
from django.http import HttpResponse
import logging

log = logging.getLogger(__name__)


def index(request):
    log.info(f"Index requested: {request}")
    return HttpResponse(
        """<H1>Hello Worldo!</H1>
                        <p><b>Hello All!</b></p>
                        <p><i>Hello, dear.</i></p>"""
    )


def about(request):
    log.info(f"About requested: {request}")
    return HttpResponse(
        """<H1>About me</H1>
                        <p><b>I'm a man!)</b></p>
                        <p><i>Pythonist-developer, low-currency system engeneer and simply good person.</i></p>"""
    )
