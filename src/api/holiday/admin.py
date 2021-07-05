from flask_admin.contrib.sqla import ModelView


class HolidayAdminView(ModelView):
    column_searchable_list = ("name",)
    column_editable_list = (
        "name",
        "date",
    )
    column_filters = (
        "name",
        "date",
    )
    column_sortable_list = (
        "name",
        "date",
        "created_date",
    )
    column_default_sort = ("date", True)
