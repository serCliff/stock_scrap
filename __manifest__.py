# -*- coding: utf-8 -*-
{
    'name': "stock_scrap",

    'summary': """
        Add costs to products to make scraps better
        - The last cost of purchase will be added to cost of product
        
        Add cost of product to stock.scrap
        
        """,



    'description': """
        Long description of module's purpose
    """,

    'author': "Sergio Del Castillo Baranda",
    'website': "http://www.sergiodelcastillo.com",


    'category': 'stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock','purchase'],

    # always loaded
    'data': [
        'data/action_set_costs.xml',
        'views/stock_scrap.xml',
    ],

}