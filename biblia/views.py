from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from biblia.models import Verse, Book, Version, Chapter
from anotacoes.models import Note  # Ajuste para o nome real do seu modelo de anotações
from django.db.models import Min, Max

def home(request, id_livro=None, id_capitulo=None):

    if id_livro != None and id_capitulo == None:
        id_capitulo = 1
    else:
        id_capitulo = id_capitulo or request.COOKIES.get('capitulo', 1)
    # Parâmetros que podem ser passados via URL ou como parâmetros GET
    id_livro = id_livro or request.COOKIES.get('livro', 'gn')
    
    
    nome_livro = request.GET.get('livro', id_livro)  # Exemplo: 'João'
    id_versao = request.GET.get('versao', 'nvi')  # Exemplo: 'nvi'
    capitulo = int(request.GET.get('capitulo', id_capitulo))  # Exemplo: 4
    # Buscar todos os livros disponíveis
    books = Book.objects.all()

    # Buscar o objeto do livro especificado, ou padrão se não especificado
    book = get_object_or_404(Book, id=nome_livro)
    
    chaps = Chapter.objects.filter(book=book)
    # Buscar o objeto da versão especificada, ou padrão se não especificado
    version = get_object_or_404(Version, id=id_versao)
    
    # Buscar todos os versículos do capítulo especificado na versão especificada
    verses = Verse.objects.filter(book=book, chapter=capitulo, version=version)
    
    # Calcular o mínimo e o máximo número de versículo
    verses_min = verses.order_by('number').first().number if verses.exists() else None
    verses_max = verses.order_by('-number').first().number if verses.exists() else None
    
    # Adapte a busca de anotações para considerar o capítulo e versão especificados
    annotations = Note.objects.filter(
        ranges__version=version,
        ranges__start_book=book,
        ranges__start_chapter=capitulo,
        ranges__end_book=book,
        ranges__end_chapter=capitulo
    ).distinct()

    # Ajuste para incluir start_verse e end_verse nas anotações
    for annotation in annotations:
        ranges = annotation.ranges.all()
        if ranges:
            annotation.start_verse = f"{ranges[0].start_book.name} {ranges[0].start_chapter}:{ranges[0].start_verse}"
            annotation.end_verse = f"{ranges[0].end_verse}"
        else:
            annotation.start_verse = "N/A"
            annotation.end_verse = "N/A"

    context = {
        'verses': verses,
        'version': version,
        'book': book,
        'chapter': capitulo,
        'verses_min': verses_min,
        'verses_max': verses_max,
        'annotations': annotations,
        'books': books,
        'chaps': chaps
    }

    # Criar a resposta renderizada
    response = render(request, 'home.html', context)

    # Definir um cookie na resposta
    # O cookie 'versao_escolhida' expirará em 30 dias
    response.set_cookie('livro', id_livro, max_age=30*24*60*60)
    response.set_cookie('capitulo', id_capitulo, max_age=30*24*60*60)

    return response

# Novas views para AJAX
def livros_list(request):
    livros = Book.objects.all().values('id', 'name')
    return JsonResponse(list(livros), safe=False)

def capitulos_por_livro(request, id_livro):
    # Buscar o objeto do livro especificado, ou padrão se não especificado
    nome_livro = request.GET.get('livro', id_livro)  # Exemplo: 'João'
    id_versao = request.GET.get('versao', 'nvi')  # Exemplo: 'nvi'
    capitulo = int(request.GET.get('capitulo', 1))  # Exemplo: 4
    book = get_object_or_404(Book, id=nome_livro)
    capitulos = Verse.objects.filter(book=book.name).values('chapter').distinct()
    capitulos_list = [{'id': c['chapter'], 'numero': c['chapter']} for c in capitulos]

    # Buscar todos os livros disponíveis
    books = Book.objects.all()

    
    # Buscar o objeto da versão especificada, ou padrão se não especificado
    version = get_object_or_404(Version, id=id_versao)
    
    # Buscar todos os versículos do capítulo especificado na versão especificada
    verses = Verse.objects.filter(book=book, chapter=capitulo, version=version)
    
    # Calcular o mínimo e o máximo número de versículo
    verses_min = verses.order_by('number').first().number if verses.exists() else None
    verses_max = verses.order_by('-number').first().number if verses.exists() else None
    
    # Adapte a busca de anotações para considerar o capítulo e versão especificados
    annotations = Note.objects.filter(
        ranges__version=version,
        ranges__start_book=book,
        ranges__start_chapter=capitulo,
        ranges__end_book=book,
        ranges__end_chapter=capitulo
    ).distinct()

    # Ajuste para incluir start_verse e end_verse nas anotações
    for annotation in annotations:
        ranges = annotation.ranges.all()
        if ranges:
            annotation.start_verse = f"{ranges[0].start_book.name} {ranges[0].start_chapter}:{ranges[0].start_verse}"
            annotation.end_verse = f"{ranges[0].end_verse}"
        else:
            annotation.start_verse = "N/A"
            annotation.end_verse = "N/A"

    context = {
        'verses': verses,
        'version': version,
        'book': book,
        'chapter': capitulo,
        'verses_min': verses_min,
        'verses_max': verses_max,
        'annotations': annotations,
        'books': books,
        "capitulos_list":capitulos_list
    }

    return JsonResponse(context)

def versiculos_por_capitulo(request, id_livro, id_capitulo):
    versiculos = Verse.objects.filter(book=id_livro, chapter=id_capitulo).values('verse', 'number')
    return JsonResponse(list(versiculos), safe=False)
