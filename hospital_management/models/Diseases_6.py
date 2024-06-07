from odoo import models,fields, api

class Diseases(models.Model):
    _name='hospital.diseases'
    _description='diseases'

    _rec_name='diseases_name'

    diseases_name=fields.Char(string='Diseases')
    code = fields.Char(string='Code', size=5)

    def name_get(self):

        diseases_list = []
        for diseases in self:
            dis = ''
            if diseases.code:
                dis += '[' + diseases.code + '] '
            dis += diseases.diseases_name

            print("_____________________",diseases.id)
            print("________",diseases)
            diseases_list.append((diseases.id, dis))
        return diseases_list


    @api.model
    def name_create(self,diseases_name):
        vals = {
            'diseases_name': diseases_name,
            'code': diseases_name[:3].upper()
        }
        diseases_name = self.create(vals)
        print("___****___________create name ",diseases_name)

        return diseases_name.name_get()[0]

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):

        if not args:
            args = []
        args += ['|', ('diseases_name', operator, name), ('code', operator, name)]
        diseases = self.search(args)

        print("_________NAME", name)
        print("_________ARGS", args)
        print("_________OP", operator)
        print("_________LIMIT", limit)
        return diseases.name_get()


