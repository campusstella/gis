# -*- coding: utf-8 -*-
"""
Created on 2016年9月23日

@author: user
"""
from django.shortcuts import render
import MySQLdb
from untitled.model.domain import Domain


def index(request):
    db = MySQLdb.connect("localhost", "root", "123456", "test")
    cursor = db.cursor()
    cursor.execute("select id,name,area,acolor from t_domain where pid=0")
    results = cursor.fetchall()
    data = []
    for row in results:
        model = Domain()
        model.id = row[0]
        model.name = row[1]
        model.area = row[2]
        model.acolor = row[3]
        data.append(model)

    context = {}
    context["domain"] = data
    return render(request, 'index.html', context)
