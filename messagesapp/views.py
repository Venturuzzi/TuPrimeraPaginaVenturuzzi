from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    msgs = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'messagesapp/inbox.html', {'messages_list': msgs})

@login_required
def sent(request):
    msgs = Message.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'messagesapp/sent.html', {'sent_messages': msgs})

@login_required
def compose(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('messagesapp:sent')
    else:
        form = MessageForm()
    return render(request, 'messagesapp/compose.html', {'form': form})

@login_required
def thread(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if msg.receiver == request.user:
        msg.is_read = True
        msg.save()
    return render(request, 'messagesapp/thread.html', {'message': msg})
