from django.views.generic import TemplateView

class CartView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # بيانات وهمية "تشبه" قاعدة البيانات
        dummy_cart = [
            {
                'id': 1,
                'title': 'chair',
                'image': 'https://theamishhouse.com/cdn/shop/products/theodore-side-chair-260327_847ac408-9f9f-4ba3-8dbc-10a9fc08257d.jpg?crop=center&height=1200&v=1734560346&width=1200',
                'price': 10.00,
                'quantity': 2,
            },
            {
                'id': 2,
                'title': 'pen',
                'image': 'https://www.onlinemantra.in/cdn/shop/products/PRP_AMB_WHT_CT_BP_032912_1200x1200.jpg?v=1747112155',
                'price': 15.00,
                'quantity': 1,
            },
        ]

        for item in dummy_cart:
            item['total'] = item['price'] * item['quantity']

        context['cart_items'] = dummy_cart
        context['total_price'] = sum(item['total'] for item in dummy_cart)

        return context
