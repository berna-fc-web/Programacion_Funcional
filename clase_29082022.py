#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Interpolacion de cadenas 
name = "Berna"
edad = 19
print("Hola",name,"tienes",edad,"años")


# In[2]:


#fstrings
mensaje = f"Hola {name}, tienes {edad} años"
mensaje


# In[3]:


print(mensaje)


# In[4]:


print(f"Hola {name}, tienes {edad} años")


# In[6]:


def saludo():
    print("Hola mundo")


# In[7]:


saludo()#se esta invocando la funcion


# In[10]:


mi_funcion=saludo()#se esta asignando la funcion 


# In[11]:


print(mi_funcion)


# In[12]:


def saludo2():
    return "HOLA MUNDO"


# In[13]:


saludo2()#invocacion


# In[14]:


mi_funcion2=saludo2()


# In[15]:


print(mi_funcion2)


# In[16]:


a=5
b=10
res=f"la suma es {a} + {b} 0 {a+b}"
print(res)


# In[17]:


def suma(a,b):
    return a+b


# In[20]:


res = f"la suma es {a} + {b} = {suma(a,b)}"


# In[21]:


print(res)


# In[24]:


lista_numeros = ["uno", "dos", "tres"]
msg_numeros= f"numeros: {lista_numeros}"
print(msg_numeros)


# In[25]:


tupla_numeros = ("uno", "dos" ,"tres")
msg_numeros= f"numeros: {tupla_numeros}"
print(msg_numeros)


# In[26]:


set_numeros = {"uno", "dos" ,"tres","tres"}
print(set_numeros)


# In[28]:


dict_numero = {"1": "uno", "2": "dos", "3": "tres"}
msg_dict_numeros = f"Numeros: {dict_numero}"
print(dict_numero)


# In[29]:


dos= f"Numeros: {dict_numero['2']}"
print(dos)


# In[30]:


"""
Escriba una funcion que mediate strings retorne el mensaje "Hola <nombre> tienes <edad> años".
Los argumentos de la funcion son: año actual, año de nacimiento y nombre.
"""


# In[44]:


def mensaje(nombre:int ,año_actual: int, año_naci:int)->str :
    return f"Hola {nombre} tienes {año_actual-año_naci} años"
print(mensaje("Berna",2022,2002))


# In[51]:


num_materias=["No.",1,2,3,4]
name_materia=[
    "Materia",
    "Estructura de datos",
    "Ecuaciones Diferenciales",
    "Metodos Numericos",
    "Programación Funcional"
]
name_profesor=[
    "Profesor",
    "Soto",
    "Ely",
    "Edgar",
    "Walter"
]

for i in range(5):
    print(f"{num_materias[i]:^5}{name_materia[i]:^30}{name_profesor[i]:^10}")




# In[ ]:




