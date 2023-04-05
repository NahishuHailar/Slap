menu = [{'title': "О проекте", 'url_name': 'home'},
        {'title': "Учителям", 'url_name': 'mentor_page'},
        {'title': "Ученикам", 'url_name': 'student_order'},
        {'title': "Работникам столовой", 'url_name': 'home'},
        ]

class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
