# -*- coding: utf-8 -*-
"""Gera o HTML estatico de flashcards e quiz (LaTeX nao sobrevive dentro de string JS)."""
import io, sys

def gera(dirg, FLASH, QUIZ):
    flash = "\n".join('  <div class="fc"><div class="frente">%s</div><div class="verso">%s</div></div>' % (f, v)
                      for f, v in FLASH)
    quiz = "\n".join(
        '<div class="q" data-c="%d"><b>%d.</b> %s\n  <div class="alts">%s</div>\n  <div class="fb">%s</div>\n</div>'
        % (c, i + 1, q, "".join('<button class="alt" data-j="%d">%s</button>' % (j, a) for j, a in enumerate(alts)), fb)
        for i, (q, alts, c, fb) in enumerate(QUIZ))
    io.open(dirg + "/_flash.frag", "w", encoding="utf-8").write(flash)
    io.open(dirg + "/_quiz.frag", "w", encoding="utf-8").write(quiz)
    print("  flash %d chars, quiz %d chars" % (len(flash), len(quiz)))

JS = """
// ---------- Feynman: salva no navegador ----------
document.querySelectorAll('textarea[data-fey]').forEach(function(ta){
  var k='rec-iedo-'+ta.dataset.fey;
  var aviso=document.querySelector('[data-salvo="'+ta.dataset.fey+'"]');
  try{ var v=localStorage.getItem(k); if(v){ta.value=v; if(aviso)aviso.textContent='\\u2713 resposta salva';} }catch(e){}
  var t=null;
  ta.addEventListener('input',function(){
    clearTimeout(t);
    t=setTimeout(function(){
      try{ localStorage.setItem(k,ta.value); if(aviso)aviso.textContent='\\u2713 salvo'; }catch(e){}
    },400);
  });
});

// ---------- Flashcards: virar ----------
document.querySelectorAll('.fc').forEach(function(c){
  c.addEventListener('click',function(){c.classList.toggle('virado');});
});

// ---------- Quiz ----------
var acertos=0, respondidas=0, total=document.querySelectorAll('.quiz .q').length;
var placar=document.getElementById('placar');
function atualiza(){placar.textContent=acertos+' / '+respondidas+(respondidas===total?' \\u2014 fim':'');}
document.querySelectorAll('.quiz .q').forEach(function(bloco){
  var certa=+bloco.dataset.c;
  bloco.querySelectorAll('button.alt').forEach(function(b){
    b.addEventListener('click',function(){
      if(bloco.dataset.feito) return;
      bloco.dataset.feito='1';
      respondidas++;
      if(+b.dataset.j===certa){acertos++;b.classList.add('certa');}
      else{
        b.classList.add('errada');
        bloco.querySelector('button.alt[data-j="'+certa+'"]').classList.add('certa');
      }
      bloco.querySelector('.fb').classList.add('on');
      atualiza();
    });
  });
});
atualiza();
"""
