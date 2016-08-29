from django.template.context import RequestContext
from django.db import connection
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render_to_response
from .models import Proyecto
from django.core.urlresolvers import reverse, reverse_lazy, resolve
from django.views.generic import RedirectView
from .forms import tipoAtribute, PostForms, data_Form
from django.http import HttpResponseRedirect
import csv
import json
import random


#######################
#Vistas
#######################

def index(request):
    arrayBases = getDatabasesIndex(request)
    return render(request, 'index.html', {
        'arrayBases': arrayBases,
    })

def chart(request):
    arrayBases = getDatabases(request)
    database_name = "lala"
    return render(request, 'SChart.html', {
        'arrayBases': arrayBases,
        'database_name': database_name,
    })


def chart2(request, database_name):
    if 'showData' in request.POST:
        database_name =  request.POST.get('DataBase')
        atributos2 = getColumnNamesWTA(database_name)
        atributos = []
        for i in atributos2:
            for j in i:
                    atributos.append(j)
        return render(request, 'pruebaChart.html', {
            'atributos': atributos,
            'database_name': database_name,
            })

    elif 'Atributos' in request.POST:
        atributo =  request.POST.get('Atributos')
        print atributo
        cursor = connection.cursor()
        cursor.execute("USE " + database_name)
        cursor.execute("SELECT COUNT(DISTINCT " + atributo +") FROM " + database_name)
        numero = cursor.fetchall()
        ArrayElement = []
        for i in numero:
            for j in i:
                ArrayElement.append(j)
        nb_element = ArrayElement[0]

        atributos2 = getColumnNamesWTA(database_name)
        atributos = []
        for i in atributos2:
            for j in i:
                    atributos.append(j)

        cursor.execute("SELECT "+ atributo +" FROM " + database_name +" GROUP BY "+ atributo)
        data = cursor.fetchall()
        ArrayData = []
        for i in data:
            for j in i:
                ArrayData.append(j)
        xdata = ArrayData

        cursor.execute("SELECT COUNT(*) FROM " + database_name +" GROUP BY "+ atributo)
        data = cursor.fetchall()
        ArrayDataY = []
        for i in data:
            for j in i:
                ArrayDataY.append(j)
        ydata = ArrayDataY
        print ydata
        extra_serie = {"tooltip": {"y_start": "Hay ", "y_end": " "}}

        chartdata = {
            'x': xdata,
            'name1': atributo, 'y1': ydata, 'extra1': extra_serie,
            }



        charttype = "multiBarChart"
        chartcontainer = 'multibarchart_container'  # container name
        chartcontainer_with_date = 'date_multibarchart_container'  # container name
        data = {
            'atributos':atributos,
            'database_name': database_name,
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'x_is_date': False,
                'x_axis_format': '',
                'tag_script_js': True,
                'jquery_on_ready': True,
                },

        }

        return render(request, 'pruebaChart.html', data)





#..........MITZI PEDORRA
def chartM(request):
    arrayBases = getDatabases(request)
    database_name = "lala"
    return render(request, 'MChart.html', {
        'arrayBases': arrayBases,
        'database_name': database_name,
    })


def chart2M(request, database_name):
    if 'showData' in request.POST:
        database_name =  request.POST.get('DataBase')
        atributos2 = getColumnNamesWTA(database_name)
        atributos = []
        for i in atributos2:
            for j in i:
                    atributos.append(j)
        return render(request, 'pruebaChartM.html', {
            'atributos': atributos,
            'database_name': database_name,
            })

    elif 'Atributos' in request.POST:
        atributo =  request.POST.get('Atributos')
        print atributo
        cursor = connection.cursor()
        cursor.execute("USE " + database_name)
        cursor.execute("SELECT COUNT(DISTINCT " + atributo +") FROM " + database_name)
        numero = cursor.fetchall()
        ArrayElement = []
        for i in numero:
            for j in i:
                ArrayElement.append(j)
        nb_element = ArrayElement[0]

        atributos2 = getColumnNamesWTA(database_name)
        atributos = []
        for i in atributos2:
            for j in i:
                    atributos.append(j)

        cursor.execute("SELECT "+ atributo +" FROM " + database_name +" GROUP BY "+ atributo)
        data = cursor.fetchall()
        ArrayData = []
        for i in data:
            for j in i:
                ArrayData.append(j)
        xdata = ArrayData

        cursor.execute("SELECT COUNT(*) FROM " + database_name +" GROUP BY "+ atributo)
        data = cursor.fetchall()
        ArrayDataY = []
        for i in data:
            for j in i:
                ArrayDataY.append(j)
        ydata = ArrayDataY
        print ydata
        extra_serie = {"tooltip": {"y_start": "Hay ", "y_end": " "}}

        chartdata = {
            'x': xdata,
            'name1': atributo, 'y1': ydata, 'extra1': extra_serie,
            }



        charttype = "stackedAreaChart"
        chartcontainer = 'stackedareachart_container'  # container name
        chartcontainer_with_date = 'date_stackedareachart_container'  # container name
        data = {
            'atributos':atributos,
            'database_name': database_name,
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'x_is_date': False,
                'x_axis_format': '',
                'tag_script_js': True,
                'jquery_on_ready': True,
                },

        }

        return render(request, 'pruebaChartM.html', data)

#...... mitzi pedorra FIN



#....... daniel pedorro grafica
def chartD(request):
    arrayBases = getDatabases(request)
    database_name = "lala"
    return render(request, 'DChart.html', {
        'arrayBases': arrayBases,
        'database_name': database_name,
    })


def chart2D(request, database_name):
    if 'showData' in request.POST:
        database_name =  request.POST.get('DataBase')
        atributos2 = getColumnNamesWTA(database_name)
        atributos = []
        for i in atributos2:
            for j in i:
                    atributos.append(j)
        return render(request, 'pruebaChartD.html', {
            'atributos': atributos,
            'database_name': database_name,
            })

    elif 'Atributos' in request.POST:
        atributo =  request.POST.get('Atributos')
        cursor = connection.cursor()
        cursor.execute("USE " + database_name)
        cursor.execute("SELECT COUNT(DISTINCT " + atributo +") FROM " + database_name)
        numero = cursor.fetchall()
        ArrayElement = []
        for i in numero:
            for j in i:
                ArrayElement.append(j)
        nb_element = ArrayElement[0]

        atributos2 = getColumnNamesWTA(database_name)
        atributos = []
        for i in atributos2:
            for j in i:
                    atributos.append(j)

        cursor.execute("SELECT id FROM " + database_name)
        xdata = get_1D_array(cursor.fetchall())
        cursor.execute("SELECT " + atributo + " FROM " + database_name)
        ydata1 = get_1D_array(cursor.fetchall())

        kwargs1 = {'shape': 'triangle-up'}

        extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}

        chartdata = {
            'x': xdata,
            'name1': atributo, 'y1': ydata1, 'kwargs1': kwargs1,
        }
        charttype = "scatterChart"
        chartcontainer = 'scatterchart_container'  # container name
        data = {
            'atributos':atributos,
            'database_name': database_name,
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'x_is_date': False,
                'x_axis_format': '',
                'tag_script_js': True,
                'jquery_on_ready': True,
            },
        }
        cursor.close()
        return render_to_response('pruebaChartD.html', data)

#........ daniel pedorro FIN


def createProject(request):
    if request.method == 'GET':
        form = PostForms()

    return render(request, 'create.html', {
        'form': form,
    })

def createBD(request):
    try:
        if request.method == 'POST':
            form = PostForms(request.POST)
            if form.is_valid():
                name = form.cleaned_data['nombreProyecto']
                proyecto = Proyecto(nombreProyecto=name)
                proyecto.save()
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE " + proyecto.nombreProyecto)
                return HttpResponseRedirect(reverse('index'))

    except:
        form = PostForms()
        exception = "exception"
        return render(request, 'create.html', {
            'form': form,
            'exception': exception
            })

def showAtributes(request):
    arrayBases = getDatabases(request)
    return render(request, 'Atribute.html', {
        'arrayBases': arrayBases,
    })


def showAtributes2(request):
    if 'showAtributo' in request.POST:
        database_name =  request.POST.get('DataBase')
        atributos = getColumnNames(database_name)
        form = data_Form(request.POST)

        return render(request, 'Atribute2.html', {
            'form': form,
            'atributos': atributos,
            'database_name': database_name,
            })


def showAtributes3(request, database_name):
    form = tipoAtribute()
    return render(request, 'createAtribute.html', {
        'form': form,
        'database_name': database_name,
    })

def showAtributes4(request, database_name):
    atributos = getColumnNames(database_name)
    form = data_Form(request.POST)
    return render(request, 'Atribute2.html', {
        'form': form,
        'atributos': atributos,
        'database_name': database_name,
        })



def createAtribute(request, database_name):
    try:
        if request.method == 'POST':
            nombreAtribute = request.POST.getlist('nombreAtribute')
            tipoAtribute = request.POST.getlist('tipoAtributo')
            cursor = connection.cursor()
            tables = getTables(database_name)
            if database_name not in tables:
                cursor.execute("use " + database_name)
                cursor.execute("CREATE TABLE "+ database_name + "( Id INT PRIMARY KEY AUTO_INCREMENT)")
                i =0
                for tipo in tipoAtribute:
                    if tipo == "Categorico":
                        cursor.execute("use " + database_name)
                        cursor.execute("ALTER TABLE "+ database_name + " ADD " + nombreAtribute[i] + " VARCHAR(25)")
                        i = i+1
                    elif tipo == "Numerico":
                        cursor.execute("use " + database_name)
                        cursor.execute("ALTER TABLE "+ database_name + " ADD " + nombreAtribute[i] + " FLOAT")
                        i = i+1

            else:
                i =0
                for tipo in tipoAtribute:
                    if tipo == "Categorico":
                        cursor.execute("use " + database_name)
                        cursor.execute("ALTER TABLE "+ database_name + " ADD " + nombreAtribute[i] + " VARCHAR(25)")
                        i = i+1
                    elif tipo == "Numerico":
                        cursor.execute("use " + database_name)
                        cursor.execute("ALTER TABLE "+ database_name + " ADD " + nombreAtribute[i] + " FLOAT")
                        i = i+1


            atributos = getColumnNames(database_name)
            form = data_Form()
            return render(request, 'Atribute2.html', {
                'form': form,
                'atributos': atributos,
                'database_name': database_name,
                })

    except:
        atributos = getColumnNames(database_name)
        exception = "exception"
        return render(request, 'Atribute2.html', {
            'exception': exception,
            'atributos': atributos,
            'database_name': database_name,
        })

def showData(request):
    arrayBases = getDatabases(request)
    return render(request, 'data.html', {
        'arrayBases': arrayBases,
    })


def showData2(request):
    if 'showData' in request.POST:
        database_name =  request.POST.get('DataBase')
        atributos = getColumnNamesWTA2(database_name)
        datos = getData(database_name, atributos)
        form = data_Form(request.POST)
        return render(request, 'showData.html', {
            'form': form,
            'atributos': atributos,
            'database_name': database_name,
            'datos': datos,
            })

def showData3(request, database_name):
    atributos = getColumnNamesWTA2(database_name)
    datos = getData(database_name, atributos)
    form = data_Form(request.POST)
    return render(request, 'showData.html', {
        'form': form,
        'atributos': atributos,
        'database_name': database_name,
        'datos': datos,
        })

def getCSVData(request, database_name):
    try:
        atributos = getColumnNamesWTA(database_name)
        arrayAtributos = []
        for i in atributos:
            for j in i:
                arrayAtributos.append(j)
        form = data_Form(request.POST, request.FILES)

        uploaded_file = request.FILES['csvArchive']
        fout = open("media/%s" % uploaded_file.name, 'wb')
        for chunk in uploaded_file.chunks():
            fout.write(chunk)
            fout.close()
        comas = []
        f = open("media/%s" % uploaded_file.name, 'rb')
        csv_f = csv.reader(f)
        header = csv_f.next()
        if len(atributos) == len(header):
            for data in csv_f:
                insertValues(request, database_name, header, data)


        #csv_f = csv.reader(f)
        #header = csv_f.next()
        #if len(atributos) == len(header):
        #    for data in csv_f:
        #        insertValues(database_name, header, data)

    #column = {}
    #for h in header:
    #    column[h] = []

    #for row in csv_f:
    #    for h, v in zip(header, row):
    #        column[h].append(v)

        form = data_Form()
        datos = getData(database_name, atributos)
        return render(request, 'showData.html', {
            'form': form,
            'atributos': atributos,
            'database_name': database_name,
            'datos': datos,
            })

    except:
        atributos = getColumnNamesWTA(database_name)
        form = data_Form()
        exception = "exception"
        return render(request, 'createData.html', {
            'form': form,
            'atributos': atributos,
            'database_name': database_name,
            'exception': exception,
            })


def createData(request, database_name):
    atributos = getColumnNamesWTA(database_name)
    form = data_Form()
    return render(request, 'createData.html', {
        'form': form,
        'atributos': atributos,
        'database_name': database_name,
        })

def createData2(request, database_name):
    if 'guardar' in request.POST:
        data = request.POST.getlist('data')
        atributos = getColumnNamesWTA(database_name)
        arrayAtributos = []
        for i in atributos:
            for j in i:
                arrayAtributos.append(j)
        insertValues(request, database_name, arrayAtributos, data)
        atributos = getColumnNamesWTA2(database_name)
        datos = getData(database_name, atributos)
        form = data_Form(request.POST)
        return render(request, 'showData.html', {
            'form': form,
            'atributos': atributos,
            'database_name': database_name,
            'datos': datos,
            })

    elif 'cancelar' in request.POST:
        atributos = getColumnNamesWTA2(database_name)
        datos = getData(database_name, atributos)
        form = data_Form(request.POST)
        return render(request, 'showData.html', {
            'form': form,
            'atributos': atributos,
            'database_name': database_name,
            'datos': datos,
            })



def deleteData(request, database_name, data):
    cursor = connection.cursor()
    cursor.execute("USE " + database_name)
    cursor.execute("DELETE FROM " + database_name + " WHERE Id = '" + data + "'")
    atributos = getColumnNamesWTA2(database_name)
    datos = getData(database_name, atributos)
    form = data_Form(request.POST)
    return render(request, 'showData.html', {
        'form': form,
        'atributos': atributos,
        'database_name': database_name,
        'datos': datos,
        })


def deleteProject(request, base):
    atributos = getColumnNames(base)
    delete = "delete"
    i = 0
    for atributo in atributos:
        i = i+1
    if i == 0:
        cursor= connection.cursor()
        cursor.execute("DELETE FROM Administration_proyecto WHERE nombreProyecto = '" + base + "'")
        cursor.execute("DROP DATABASE " + base)
        return HttpResponseRedirect(reverse('index'))
    elif i > 0:
        arrayBases = getDatabasesIndex(request)
        return render(request, 'indexNOT.html', {
            'arrayBases': arrayBases,
            'delete' : delete,
        })

def deleteAtribute(request, database_name, atributo):
    cursor = connection.cursor()
    cursor.execute("USE " + database_name)
    cursor.execute("ALTER TABLE " + database_name + " DROP COLUMN " + atributo)
    atributos = getColumnNames(database_name)
    form = data_Form(request.POST)

    return render(request, 'Atribute2.html', {
        'form': form,
        'atributos': atributos,
        'database_name': database_name,
        })

def modifyAtribute(request, database_name, atributo):
    cursor = connection.cursor()
    cursor.execute("USE " + database_name)
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = '"+ database_name + "' AND column_name = '" + atributo + "'")
    atributo = cursor.fetchall()
    atributoName = []
    for i in atributo:
        for j in i:
                atributoName.append(j)
    form = tipoAtribute()
    return render(request, 'createAtribute.html', {
        'form': form,
        'database_name': database_name,
        'atributoName': atributoName,
    })

def modifyAtribute2(request, database_name, atributoName):
    columnNew = request.POST.get('nombreAtribute')
    cursor = connection.cursor()
    cursor.execute("USE " + database_name)
    cursor.execute("SELECT data_type FROM information_schema.columns WHERE table_name = '"+ database_name + "' AND column_name = '" + str(atributoName) + "'")
    tipoo = cursor.fetchall()
    tipo = []
    for i in tipoo:
        for j in i:
            tipo.append(j)
    if "float" in tipo:
        cursor.execute("ALTER TABLE "+ database_name+ " CHANGE "+ str(atributoName) +" "+ columnNew +" " + str(tipo[0]))
    elif "varchar" in tipo:
        cursor.execute("ALTER TABLE "+ database_name+ " CHANGE "+ str(atributoName) +" "+ columnNew +" " + str(tipo[0]) + "(25)")

    atributos = getColumnNames(database_name)
    form = data_Form(request.POST)

    return render(request, 'Atribute2.html', {
        'form': form,
        'atributos': atributos,
        'database_name': database_name,
        })

def modifyData(request, database_name, data):
    Id = data
    atributos = getColumnNamesWTA(database_name)
    arrayAtributos = []
    for i in atributos:
        for j in i:
            arrayAtributos.append(j)
    atributoss = ','.join(arrayAtributos)
    cursor = connection.cursor()
    cursor.execute("USE " + database_name)
    cursor.execute("SELECT " + atributoss + " FROM " + database_name + " WHERE Id = '" + str(data) + "'")
    datos = cursor.fetchall()
    form = data_Form()
    return render(request, 'modifyData.html', {
        'form': form,
        'atributos': atributos,
        'database_name': database_name,
        'datos': datos,
        'Id': Id,
        })

def modifyData2(request, database_name, Id):
    data = request.POST.getlist('data')
    atributos = getColumnNamesWTA(database_name)
    arrayAtributos = []
    for i in atributos:
        for j in i:
            arrayAtributos.append(j)
    updateValues(database_name, arrayAtributos, data, Id)

    atributos = getColumnNamesWTA2(database_name)
    datos = getData(database_name, atributos)
    form = data_Form(request.POST)
    return render(request, 'showData.html', {
        'form': form,
        'atributos': atributos,
        'database_name': database_name,
        'datos': datos,
        })


def seleccionarAccion(request, database_name):
    accion =  request.POST.get('accion')
    if accion == 'Manual':
        atributos = getColumnNamesWTA(database_name)
        form = data_Form()
        return render(request, 'createData.html', {
            'form': form,
            'atributos': atributos,
            'database_name': database_name,
            })
    elif accion == 'Cargar archivo CSV':
        csv = "archivo csv"
        atributos = getColumnNamesWTA(database_name)
        form = data_Form()
        return render(request, 'createData.html', {
            'form': form,
            'atributos': atributos,
            'database_name': database_name,
            'csv': csv,
            })


###################
#Funciones
###################

def getDatabasesIndex(request):
    cursor= connection.cursor()
    cursor.execute("SELECT nombreProyecto FROM Administration_proyecto")
    bases = cursor.fetchall()
    return bases

def getDatabases(index):
    cursor= connection.cursor()
    cursor.execute("SELECT nombreProyecto FROM Administration_proyecto")
    bases = cursor.fetchall()
    arrayBases = []
    for i in bases:
        for j in i:
                arrayBases.append(j)
    return arrayBases

def getColumnNames(database_name):
    cursor = connection.cursor()
    cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '"+ database_name + "' AND NOT column_name = 'Id'")
    atributos = cursor.fetchall()
    return atributos

def getColumnNamesWTA(database_name):
    cursor = connection.cursor()
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = '"+ database_name + "' AND NOT column_name = 'Id'")
    atributos = cursor.fetchall()
    return atributos

def getColumnNamesWTA2(database_name):
    cursor = connection.cursor()
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = '"+ database_name + "'")
    atributos = cursor.fetchall()
    return atributos

def getTables(database_name):
    cursor= connection.cursor()
    cursor.execute("use "+ database_name)
    cursor.execute("show tables")
    tables = cursor.fetchall()
    arrayTables = []
    for i in tables:
        for j in i:
            arrayTables.append(j)
    return arrayTables

def getData(database_name, atributos):
    cursor= connection.cursor()
    cursor.execute("use "+ database_name)
    for i in atributos:
        str(i)
        cursor.execute("SELECT * FROM " + database_name)
    datos = cursor.fetchall()
    datooos = ()
    for dato in datos:
        datooos = datooos + dato[1:len(dato)]
    return datos


def insertValues(request, database_name, header, data):
    try:
        atributos = ','.join(header)
        datos = (', '.join('"' + item + '"' for item in data))
        cursor= connection.cursor()
        cursor.execute("use "+ database_name)
        cursor.execute("INSERT INTO " + database_name + "("+ atributos + ") VALUES (" + datos +")")
    except:
        atributos = getColumnNamesWTA(database_name)
        form = data_Form()
        exception = "exception"
        return render(request, 'createData.html', {
            'exception': exception,
            'form': form,
            'atributos': atributos,
            'database_name': database_name,
            })

def updateValues(database_name, arrayAtributos, data, Id):
    cursor= connection.cursor()
    cursor.execute("use "+ database_name)
    i = 0
    for atributo in arrayAtributos:
        cursor.execute("UPDATE " + database_name + " SET "+ str(arrayAtributos[i]) + " = '" + str(data[i]) +"' WHERE Id = '" + str(Id) + "'")
        i = i + 1

def get_1D_array(column):
    array1D = []
    for i in column:
        for j in i:
            array1D.append(j)
    return array1D
