from django.views.generic import TemplateView

class CheckoutView(TemplateView):
    template_name = 'orders/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items_count'] = 3
        context['shipping_cost'] = 5.00
        context['subtotal'] = 35
        context['total'] = context['subtotal'] + context['shipping_cost']

        return context