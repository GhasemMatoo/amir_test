from implementation.models import *

def resource_allocation_calc(instance, dict_data):
    instance.number_active_shifts = (dict_data["active_day_shift"] * dict_data["day_shift_hours"]) + \
                                         (dict_data["active_night_shift"] * dict_data["night_shift_hours"])
    instance.number_services_hour = (60 / ((2 * dict_data["carrying_distance"]) * 60 / 40) + 8)
    instance.hours_normal_implement_enterprise_machines = \
        (dict_data["performance"].amounts - dict_data["amounts_total_work_contractors"]) / \
        instance.number_active_shifts
    instance.impact_factor = (instance.number_active_shifts/(
        (dict_data['active_day_shift'] + dict_data["active_night_shift"])
        * (dict_data["day_shift_hours"] + dict_data["night_shift_hours"])))

    return instance


def machinery_form_calc(instance, item_name, item_amount, val):
    source = (int(val) * instance.impact_factor * instance.hours_normal_implement_enterprise_machines) / \
             int(item_amount)
    if 'لودر' in item_name:
        instance.calc_loader = source
    elif 'بلدوزر' in item_name:
        instance.calc_bulldozer = source
    elif 'بیل مکانیکی' in item_name:
        instance.calc_bil_micanici = source
    return instance
