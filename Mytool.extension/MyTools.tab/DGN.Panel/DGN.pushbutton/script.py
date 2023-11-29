from pyrevit import revit, DB, forms
doc = revit.doc
options = DB.SaveAsOptions()
dgn_path = forms.save_file("Exportar para dgn", "dgn Files (*.dgn)|*.dgn")
if dgn_path:
    try:
        doc.SaveAs(dgn_path, options)
        forms.alert("Exportacao dgn concluida com sucesso!", title="Exportar dgn")
    except Exception as e:
        forms.alert("Erro na exportacao dgn: "+str(e), title="Erro na Exportacao dgn")
else:
    forms.alert("Caminho do arquivo dgn nao especificado. Exportacao cancelada.", title="Exportar dgn")