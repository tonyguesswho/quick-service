from flask_admin.contrib.sqla import ModelView


class OrdersAdminView(ModelView):
    column_searchable_list = ("service_id", "customer_id")
    column_editable_list = (
        "customer_id",
        "created_date",
    )
    column_filters = ("customer_id",)
    column_sortable_list = (
        "customer_id",
        "created_date",
    )
    column_default_sort = ("created_date", True)
