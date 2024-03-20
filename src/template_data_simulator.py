from typing import List


class TemplateRecord:
    def __init__(self, name: str, variables: List[str], html_path: str):
        self.name = name
        self.variables = variables
        self.html_path = html_path


TEMPLATES = {
    "order_confirmation": TemplateRecord(
        "order_confirmation",
        ["customer_name", "company_name", "order_number", "order_link"],
        "templates/order_confirmation.html",
    ),
    "order_shipped": TemplateRecord(
        "order_shipped",
        [
            "customer_name",
            "company_name",
            "order_number",
            "tracking_number",
            "carrier_name",
        ],
        "templates/order_shipped.html",
    ),
}


def get_template(template_name: str):
    """
    retrieve a template record by name
    """
    if template_name not in TEMPLATES:
        raise ValueError(f"Template '{template_name}' not found")

    template_path = TEMPLATES[template_name].html_path

    try:
        with open(template_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise ValueError(f"Template file not found: {template_name}")


def get_template_variables(template_name: str) -> list:
    if template_name not in TEMPLATES:
        raise ValueError(f"Template '{template_name}' not found")
    return TEMPLATES[template_name].variables
