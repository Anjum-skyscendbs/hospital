from odoo import models,fields, api

class Diseases(models.Model):
    _name='hospital.diseases'
    _description='diseases'

    _rec_name='diseases_name'

    diseases_name=fields.Char(string='Diseases')
    code = fields.Char(string='Code', size=7)

    # Exercise-4 9. Override name_get method and display two fields rather than just name in the many2one field
    def name_get(self):
        diseases_list = []
        for diseases in self:
            dis = ''
            if diseases.code:  # Check if code exists (could be None)
               dis += '[' + diseases.code + '] '  # Convert code to string before concatenation
            dis += diseases.diseases_name
            print("_____________________", diseases.diseases_name)
            print("_____________________", diseases.id)
            print("________", diseases)
            diseases_list.append((diseases.id, dis))
        return diseases_list

    # Exercise-4 11. Override name_create method to add additional fields for creating records.
    @api.model
    def name_create(self, diseases_name):
        vals = {
             'diseases_name': diseases_name,
             'code': diseases_name[:3].upper() if diseases_name else False
       }
        diseases = self.create(vals)
        print("___****___________create name ", diseases_name)
        return diseases.name_get()[0]


# Exercise-4 10. Override name_search method to search with both the fields which are displayed in many2one field.
@api.model
def name_search(self, name='', args=None, operator='ilike', limit=100):
    if not args:
        args = []

    args += ['|', ('diseases_name', operator, name), ('code', operator, name)]
    diseases = self.search(args, limit=limit)

    print("_________NAME", name)
    print("_________ARGS", args)
    print("_________OP", operator)
    print("_________LIMIT", limit)
    return diseases.name_get()


# Exercise-4 17. Add an onchange method which will add a domain on a many2one and many2many field.
@api.onchange('diseases_name')
def _onchange_diseases_name(self):
    if self.diseases_name:
        domain = {
            'domain': [
                ('code', '=', self.env['hospital.diseases'].search([('diseases_name', '=', self.diseases_name)]).code)]
        }
        return domain
    return {}