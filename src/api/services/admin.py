from flask_admin.contrib.sqla import ModelView


class ServiceAdminView(ModelView):
    column_searchable_list = ("name",)
    column_editable_list = (
        "name",
        "duration",
        "created_date",
    )
    column_filters = (
        "name",
        "duration",
    )
    column_sortable_list = (
        "name",
        "duration",
        "created_date",
    )
    column_default_sort = ("created_date", True)
