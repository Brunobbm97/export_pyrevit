from pyrevit import revit, DB, forms
doc = revit.doc
options = DB.SaveAsOptions()
ifc_path = forms.save_file("Exportar para IFC", "IFC Files (*.ifc)|*.ifc")
if ifc_path:
    try:
        doc.SaveAs(ifc_path, options)
        forms.alert("Exportacao IFC concluida com sucesso!", title="Exportar IFC")
    except Exception as e:
        forms.alert("Erro na exportacao IFC: "+str(e), title="Erro na Exportacao IFC")
else:
    forms.alert("Caminho do arquivo IFC nao especificado. Exportacao cancelada.", title="Exportar IFC")