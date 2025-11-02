from django.shortcuts import render, redirect
from corpo.models import Corpo
from django.contrib import messages

def formulario_corpo_view(request):
    if request.method == 'POST':
        tgc = float(request.POST['tgc'])
        musculo = float(request.POST['musculo'])
        umidade = float(request.POST['umidade'])
        massa_ossea = float(request.POST['massa_ossea'])
        tmb = float(request.POST['tmb'])
        taxa_proteica = float(request.POST['taxa_proteica'])
        idade_corporal = int(request.POST['idade_corporal'])
        gordura_viceral = int(request.POST['gordura_viceral'])
        gordura_subcutanea = float(request.POST['gordura_subcutanea'])
        peso_ideal = float(request.POST['peso_ideal'])
        gordura_corporal = float(request.POST['gordura_corporal'])
        peso_sem_gordura = float(request.POST['peso_sem_gordura'])
        peso_muscular = float(request.POST['peso_muscular'])
        quantidade_proteina = float(request.POST['quantidade_proteina'])

        # cria o objeto e salva no banco
        Corpo.objects.create(
            tgc=tgc,
            musculo=musculo,
            umidade=umidade,
            massa_ossea=massa_ossea,
            tmb=tmb,
            taxa_proteica=taxa_proteica,
            idade_corporal=idade_corporal,
            gordura_viceral=gordura_viceral,
            gordura_subcutanea=gordura_subcutanea,
            peso_ideal=peso_ideal,
            gordura_corporal=gordura_corporal,
            peso_sem_gordura=peso_sem_gordura,
            peso_muscular=peso_muscular,
            quantidade_proteina=quantidade_proteina
        )

        messages.success(request, "Dados salvos com sucesso!")
        return redirect('formulario_corpo.html')  # mantém na mesma página ou redireciona onde quiser

    return render(request, 'formulario_corpo.html')
