from django.shortcuts import render, HttpResponse

def car1(request):
    return HttpResponse(
        """
<img src="https://dkstatics-public.digikala.com/digikala-products/aaed706f5049a16f2f956bf82973e99657933c78_1681389415.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/format,webp/quality,q_90" alt="a picture">
"""
    )


def car2(request):
    return HttpResponse(
        """
<img src="https://dkstatics-public.digikala.com/digikala-products/79931cce9dc6ab069c9a36266d59d65b47b48de1_1671113186.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/format,webp/quality,q_90" alt="a picture">
"""
    )


def car3(request):
    return HttpResponse(
        """
<img src="https://dkstatics-public.digikala.com/digikala-products/3595391.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/format,webp/quality,q_90" alt="a picture">
"""
    )

def lego(request):
    return HttpResponse(
        """
<img src="https://media.imna.ir/d/2023/03/24/4/1855294.jpg?ts=1679604236000" alt="a picture">
"""
    )
