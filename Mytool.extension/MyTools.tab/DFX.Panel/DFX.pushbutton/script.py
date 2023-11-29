from pyrevit import revit, DB, forms
doc = revit.doc
options = DB.SaveAsOptions()
dfx_path = forms.save_file("Exportar para dfx", "dfx Files (*.dfx)|*.dfx")
if dfx_path:
    try:
        doc.SaveAs(dfx_path, options)
        forms.alert("Exportacao dfx concluida com sucesso!", title="Exportar dfx")
    except Exception as e:
        forms.alert("Erro na exportacao dfx: "+str(e), title="Erro na Exportacao dfx")
else:
    forms.alert("Caminho do arquivo dfx nao especificado. Exportacao cancelada.", title="Exportar dfx")