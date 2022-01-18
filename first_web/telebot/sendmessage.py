import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone):
    '''Раб оповещатель'''
    if TeleSettings.objects.get(pk=1): # Проверка на наличие данных
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        '''Делаем отображение контактых данных в телеграмме'''
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):# Проверка на наличие
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}')+1:text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]

            text_slise = part_1 + tg_name + part_2 + tg_phone + part_3 # Выводим имя и номер заявки

        else:
            text_slise = text


        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slise
                    })
        except:
            pass

        finally:
            if req.status_code != 200:
                print('Ошибка отправка')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Всё хорошо. Отправлено!')
    else:
        pass
