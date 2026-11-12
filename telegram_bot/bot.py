import telebot
from config.config import TOKEN
from services.validacao_usuario import identificar_usuario
from services.registrar_gasto import registrar_gastos
from services.registrar_gasto import resumo

#CONEXÃO COM BOT

bot = telebot.TeleBot(TOKEN)

#Start
@bot.message_handler(commands=["start"])
def receber_mensagens(mensagem):

   chat_id = mensagem.chat.id
   usuario = identificar_usuario(chat_id)
   bot.send_message(chat_id, f"Bem vindo {usuario}!\nComandos:"
      f"\nRegistra gastos: /gasto\nResumo planilha: /resumo"
      )

#registrar gasto
@bot.message_handler(commands=["gasto"])
def comando_gasto(mensagem):
   chat_id = mensagem.chat.id
   msg = bot.send_message(chat_id, "Qual valor R$: ")
   bot.register_next_step_handler(msg, receber_valor)


def receber_valor(mensagem):
   chat_id = mensagem.chat.id
   valor = float(mensagem.text.replace(",", "."))

   msg = bot.send_message(chat_id, "Qual descrição?")
   bot.register_next_step_handler(msg, receber_descricao, valor)


def receber_descricao(mensagem, valor):
   chat_id = mensagem.chat.id
   descricao = mensagem.text

   registrar_gastos(chat_id, valor, descricao)
   bot.send_message(chat_id, f"Gasto salvo:\nR$ {valor:.2f} - {descricao}")
   bot.send_message(chat_id, f"Comandos:\nRegistra gastos: /gasto\nResumo planilha: /resumo")

@bot.message_handler(commands=["resumo"])
def comando_resumo(mensagem):
    dados = resumo()
    bot.send_message(mensagem.chat.id, f"{dados}")


# INICIAR O BOT
def iniciar_bot():
   print("Bot iniciado! Aguardando mensagens...")
   bot.infinity_polling()