from django.views.generic import TemplateView
class OrderHistoryView(TemplateView):
    template_name = 'historyorder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['orders'] = [

            {
                'id': 101,
                'date': '3 August 2025',
                'status': 'Delivered',
                'status_color': 'success',
                'items': [
                    {'name': 'Fifa 19', 'quantity': 2, 'price': 10, 'total': 20},
                    {'name': 'PS4 Controller', 'quantity': 1, 'price': 30, 'total': 30},
                ],
                'total': 50,
            },
            {
                'id': 102,
                'date': '1 August 2025',
                'status': 'Pending',
                'status_color': 'warning',
                'items': [
                    {'name': 'Headphones', 'quantity': 1, 'price': 40, 'total': 40},
                ],
                'total': 40,
            },
        ]

        return context
