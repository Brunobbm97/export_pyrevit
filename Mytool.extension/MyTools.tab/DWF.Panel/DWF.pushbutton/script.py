from pyrevit import revit, DB, forms
doc = revit.doc
options = DB.SaveAsOptions()
dwg_path = forms.save_file("Exportar para dwg", "dwg Files (*.dwg)|*.dwg")
if dwg_path:
    try:
        doc.SaveAs(dwg_path, options)
        forms.alert("Exportacao dwg concluida com sucesso!", title="Exportar dwg")
    except Exception as e:
        forms.alert("Erro na exportacao dwg: "+str(e), title="Erro na Exportacao dwg")
else:
    forms.alert("Caminho do arquivo dwg nao especificado. Exportacao cancelada.", title="Exportar dwg")