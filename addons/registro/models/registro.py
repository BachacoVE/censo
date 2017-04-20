# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the Odoo plugin for Dia !
from openerp import api, fields, models

class Persona(models.Model):
    """Modelo que se utiliza para registrar los datos basicos de cada participante del curso"""
    _name = 'regtil.persona'
    _rec_name = 'cedula'
    cedula = fields.Integer(string='Cedula', help='Ingrese su cédula en el formato 16123123')
    primer_nombre = fields.Char(string= 'Primer Nombre', help='Ingrese su primer nombre. Ejemplo: Crisbel')
    segundo_nombre = fields.Char(string= 'Segundo Nombre', help='Ingrese su segundo nombre Ejemplo: Francisas')
    primer_apellido = fields.Char(string= 'Primer apellido', help='Ingrese su Primer apellido Ejemplo: Pinzon')
    segundo_apellido = fields.Char(string='Segundo Apellido', help='Ingrese su segundo Apellido Ejemplo: Villarroel')
    sexo = fields.Selection([('M','Masculino'),('F','Femenino')], string='Sexo', help='Seleccione su sexo')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', help='Selecciones su fecha de nacimiento. Seleccionando la fecha en el asistente o escribiendola en el formato 01/01/1999')
    direccion = fields.Text('Dirección', help='Ingrese su direccion de habitación')
    telefono = fields.Char(string='Télefono', help='Ingrese su télefono en el formato 04149355744')
    email = fields.Char(string='Correo Electronico', help='Ingrese su correo electronico en el formato ejempli@ejemplo.com')
    vinculacion_til_id = fields.Many2one('regtil.tipo_vinculacion_til', string ='Vinculacion TIL' , help='Selección el Tipo de Vinculacion con las TIL')
    state_id = fields.Many2one('res.country.state', string='Estado')
    municipality_id = fields.Many2one('res.country.state.municipality', string='Municipio')
    parish_id = fields.Many2one('res.country.state.municipality.parish', string='Parroquia')
    vivienda_ids = fields.One2many('regtil.vivienda', 'persona_id',string='Información de Vivienda')
    socio_economico_ids = fields.One2many('regtil.socio_economico','persona_id',string='Informacón Socio-Económica')
    unidad_productiva_ids = fields.Many2many('regtil.unidad_productiva', string='Unidad productiva')

class TipoVinculacionTIL(models.Model):
    """Tipo de Vinculación con las Tecnologías Libres"""
    _name = 'regtil.persona.tipo_vinculacion_til'
    name = fields.Char('Nombre')
    description = fields.Text('Descripción')

class Vivienda(models.Model):
    """Registro vivienda clase persona"""
    _name = 'regtil.vivienda'
    _rec_name = 'fecha_registro'
    tipo_id = fields.Many2one('regtil.vivienda.tipo', string='Tipo', help='seleccione el tipo de vivienda actual')
    tenencia_id = fields.Many2one('regtil.vivienda.tenencia', string='Tenencia', help='Seleccione el tipo de tenencia de su viviend')
    condicion_id = fields.Many2one('regtil.vivienda.condicion', string='Condicion', help='Seleccione la condicion de la vivienda ')
    tiene_television = fields.Boolean(string='¿Tiene Television?', help='la persona tildará si posee television')
    tiene_computadora = fields.Boolean(string='¿Tiene Computadora?', help='la persona tildará si posee computadora')
    tiene_internet = fields.Boolean(string='¿Tiene Internet=', help='la persona tildará si posee internet')
    persona_id = fields.Many2one('persona',string='Persona')

class ViviendaTipo(models.Model):
    """Condición de la vivienda"""
    _name="regtil.vivienda.tipo"
    name = fields.Char('Nombre')
    description = fields.Text('Descripción')

class ViviendaTenencia(models.Model):
    """Condición de la vivienda"""
    _name="regtil.vivienda.tenencia"
    name = fields.Char('Nombre')
    description = fields.Text('Descripción')

class ViviendaCondicion(models.Model):
    """Condición de la vivienda"""
    _name="regtil.vivienda.condicion"
    name = fields.Char('Nombre')
    description = fields.Text('Descripción')

class SocioEconomico(models.Model):
    """registra el nivel socio ecnonomico de la persona"""
    _name = 'regtil.socio_economico'
    _rec_name = 'ingreso_mensual'
    #Cambiar discapacidad a modelo m2m
    estado_civil =fields.Selection([('S','Soltero(a)'),('C','Casado(a)'),('Se','Separado(a)'),('Di','Divorciado(a)'),('Vi','Viudo(a)')],string='Estado civil', help='La persona podra espicificar el estado civil')
    discapacidad = fields.Boolean(string='¿posee alguna discapacidad?', help='la persona nombrara si tiene alguna discapacidad')
    cantidad_hijos = fields.Integer(string='Cant. Hijos', help='Indique cuantos hijos tiene')
    grupo_familiar = fields.Integer(string='Cant. Grupo Familiar', help='Cuantas personas componen su grupo familiar')
    trabaja = fields.Boolean(string='¿Trabaja actualmente?', help='la persona indacara si posee trabajo')
    ingreso_mensual = fields.Float(string='Ingreso Mensual', help='Indique su ingreso mensual')
    ocupacion_id = fields.Many2one('regtil.socio_economico.ocupacion',string='Ocupacion', help='Seleccione su Ocupacion ')
    grado_instruccion_id= fields.Many2one('regtil.socio_economico.grado_instruccion',string='Grado instruccion', help='Seleccione su grado_instruccion')
    persona_id = fields.Many2one('persona',string='Persona')
    
class SocioEconomicoOcupacion(models.Model):
    """Modelo que registra profesion de la persona"""
    _name = 'regtil.socio_economico.ocupacion'
    name = fields.Char('Nombre')
    description = fields.Text('Descripción')

class SocioEconomicoGradoInstruccion(models.Model):
    """Modelo que registra profesion de la persona"""
    _name = 'regtil.socio_economico.grado_instruccion'
    name = fields.Char('Nombre')
    description = fields.Text('Descripción')

class UnidadProductiva(models.Model):
    """Unidad Productiva o Comunidad a la que pertence"""
    _name = 'regtil.unidad_productiva'
    name = fields.Char(string='Nombre', help='Nombre de la unidad productiva o Comunidad')
    tipo = fields.Selection([('C','Comunidad'),('UP','Unidad Productiva'),('CyUP','Ambas')], string='Tipo', help='Tipo')
    figura_juridica_id = fields.Many2one('regtil.unidad_productiva.figura_juridica',string='Figura Jurídica', help="Indique la figura jurídica") 
    rif = fields.Integer(string='RIF', help='Ingrese su RIF en el formato J123456789')
    email = fields.Char(string='Correo Electrónico', help='Ingrese su correo electrónico en el formato ejemplo@ejemplo.com')
    telefono = fields.Char(string='Télefono', help='Ingrese el télefono en el formato 04149355744')
    website = fields.Char(string='Página Web', help='Ingrese su dirección web en el fomato http://www.ejemplo.com.ve')
    facebook = fields.Char(string='Facebook', help='Ingrese su cuenta de facebook')
    twitter = fields.Char(string='Twitter', help='Ingrese su cuenta de twitter')
    actividad_ids = fields.Many2many('regtil.unidad_productiva.actividad',string='Actividad', help='Ingresa las actividades a las que se dedica su Comunidad/UP')
    tecnologia_ids = fields.Many2many('tecnologia', string='Tecnologia')
    personas_ids = fields.Many2many('persona', string='Persona')

class UnidadProductivaFiguraJuridica(models.Model):
    """Lista de figuradas jurídicas según el código de comercio venezolano y las leyes del poder popular"""
    _name = 'regtil.unidad_productiva.figura_juridica'
    name = fields.Char('Nombre')
    description = fields.Text('Descripción')

class UnidadProductivaActividad(models.Model):
    """Lista de figuradas jurídicas según el código de comercio venezolano y las leyes del poder popular"""
    _name = 'regtil.unidad_productiva.actividad'
    name = fields.Char('Nombre')
    description = fields.Text('Descripción')
