from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import User

def home(request):
    """
    View para a página inicial.
    No Django, as Views são o equivalente aos Controllers no MVC tradicional.
    """
    return render(request, 'users/home.html', {
        'title': 'MVC com Django',
        'message': 'Bem-vindo ao exemplo MVC com Django!'
    })

def user_list(request):
    """
    View para listar todos os usuários.
    """
    users = User.objects.all()
    return render(request, 'users/user_list.html', {
        'title': 'Lista de Usuários',
        'users': users
    })

def user_detail(request, pk):
    """
    View para exibir detalhes de um usuário específico.
    """
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {
        'title': f'Usuário: {user.name}',
        'user': user
    })

def user_create(request):
    """
    View para criar um novo usuário.
    """
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            age = request.POST.get('age')
            
            # Validação simples
            if not name or not email or not age:
                messages.error(request, 'Todos os campos são obrigatórios.')
                return render(request, 'users/user_form.html', {
                    'title': 'Criar Novo Usuário',
                    'form_action': 'create'
                })
            
            # Verificar se email já existe
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Este email já está em uso.')
                return render(request, 'users/user_form.html', {
                    'title': 'Criar Novo Usuário',
                    'form_action': 'create',
                    'form_data': {'name': name, 'email': email, 'age': age}
                })
            
            # Criar usuário
            user = User.objects.create(
                name=name,
                email=email,
                age=int(age)
            )
            
            messages.success(request, f'Usuário {user.name} criado com sucesso!')
            return redirect('user_list')
            
        except ValueError:
            messages.error(request, 'Idade deve ser um número válido.')
        except Exception as e:
            messages.error(request, f'Erro ao criar usuário: {str(e)}')
    
    return render(request, 'users/user_form.html', {
        'title': 'Criar Novo Usuário',
        'form_action': 'create'
    })

def user_edit(request, pk):
    """
    View para editar um usuário existente.
    """
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            age = request.POST.get('age')
            
            # Validação simples
            if not name or not email or not age:
                messages.error(request, 'Todos os campos são obrigatórios.')
                return render(request, 'users/user_form.html', {
                    'title': f'Editar: {user.name}',
                    'form_action': 'edit',
                    'user': user
                })
            
            # Verificar se email já existe (exceto para o próprio usuário)
            if User.objects.filter(email=email).exclude(pk=pk).exists():
                messages.error(request, 'Este email já está em uso.')
                return render(request, 'users/user_form.html', {
                    'title': f'Editar: {user.name}',
                    'form_action': 'edit',
                    'user': user
                })
            
            # Atualizar usuário
            user.name = name
            user.email = email
            user.age = int(age)
            user.save()
            
            messages.success(request, f'Usuário {user.name} atualizado com sucesso!')
            return redirect('user_detail', pk=user.pk)
            
        except ValueError:
            messages.error(request, 'Idade deve ser um número válido.')
        except Exception as e:
            messages.error(request, f'Erro ao atualizar usuário: {str(e)}')
    
    return render(request, 'users/user_form.html', {
        'title': f'Editar: {user.name}',
        'form_action': 'edit',
        'user': user
    })

def user_delete(request, pk):
    """
    View para deletar um usuário.
    """
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        user_name = user.name
        user.delete()
        messages.success(request, f'Usuário {user_name} deletado com sucesso!')
        return redirect('user_list')
    
    return render(request, 'users/user_confirm_delete.html', {
        'title': f'Deletar: {user.name}',
        'user': user
    })
