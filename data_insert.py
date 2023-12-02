# Config for debug and setup Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()
# import madel and library
from implementation.models import PriceList
from datetime import datetime
import pandas as pd


def insert_price_list():
    price_lists = []
    # Get data in to excel for create Person
    df = pd.read_excel('1.xlsx', sheet_name='فهرست بها')
    standard_nan_row = df
    for row_number in range(2, len(standard_nan_row)):
        chapter_number = standard_nan_row.values[row_number][1]
        item_number = standard_nan_row.values[row_number][2]
        description = standard_nan_row.values[row_number][3]
        unit = standard_nan_row.values[row_number][4]
        amounts = standard_nan_row.values[row_number][2]
        price_list = PriceList(chapter_number=chapter_number, item_number=item_number,
                               description=description, unit=unit, amounts=amounts)
        price_lists.append(price_list)
    PriceList.objects.bulk_create(price_lists)


if __name__ == '__main__':
    # insert_address_person(),
    # inset_phone()
    # insert_state_and_city(),
    # insert_patient_status(),
    insert_price_list(),
