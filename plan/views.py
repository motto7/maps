from django.shortcuts import render, get_object_or_404, redirect
from plan.models import Post
from plan.forms import PostForm, TransitForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def total(request):
    plan_list=Post.objects.all()

    return render(request,"plan/total.html", {
        'plan_list': plan_list
        })

@login_required
def index(request):
    plan_list = Post.objects.all()
    return render(request, "plan/myplans.html", {
        'plan_list': plan_list
        })


@login_required
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    plan_list = Post.objects.all()

    tmp = post.lnglat.split('||')
    coordinate = []

    for i in range(1, len(tmp)):
        coordinate.append(tmp[i].split(','))

    return render(request, 'plan/detail.html', {
        'plan_list': plan_list,
        'post': post,
        'coordinate': coordinate,
        })


@login_required
def create_plan(request):
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            #form.save_m2m()

            messages.success(request, "새 계획이 추가되었습니다.")

            return redirect('plan:index')

    else:
        form = PostForm()

    return render(request, "plan/form.html", {
        'form': form,
        })


@login_required
def edit_plan(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            messages.info(request, "수정이 되었습니다.")
            return redirect('magazine:index')

    else:
        form = PostForm(instance=post)

    return render(request, "plan/form.html", {
        'form': form,
    })


@login_required
def add_transit(request, pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = TransitForm(request.POST)

        if form.is_valid():
            transit = form.save()
            post.transits.add(transit)

            return redirect('plan:detail',pk)
    else:
        form = TransitForm()


    return render(request, 'plan/form.html', {
            'form':form,
        })


@login_required
def index_transit(request,pk):
    post = get_object_or_404(Post, pk=pk)

    sum_tr=0

    for i in post.transits.filter():
       sum_tr+=i.cost

    return render(request, "plan/transit.html", {
        'post': post,
        'sum': sum_tr,
        })



def new_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            if request.is_ajax():
                return render(request, 'magazine/comment_row.html', {
                    'comment': comment
                    });

            else:

                messages.info(request, "댓글이 추가되었습니다.")
                return redirect('plan:detail', pk)

    else:
        form = CommentForm()

    params = {
        'form': form,
    }
    return render(request, "plan/form.html", params)