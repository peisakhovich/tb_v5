Тестовая задача по построению AZURE App service  по теме "Телеграм бот"

Постановка задачи:

Имеется в наличии:

Телегам канал "pga News Monitor" 
В администраторах котрого назначен телеграм бот "Pga News Monitor Bot"

Для взаимодействия с каналом через механизм web hoocking
будем использовать сервис

AZURE service: "test-tb-001"
    owner:  grigoriy.peisakhovlch@gmail.com
    subscription: "Azure subscription 1"
    resourceGroup: "tg-bots-rg"
    appCommandLine: "python -m uvicorn main:app --host 0.0.0.0 --port 8000"
    defaultHostName: "test-tb-001-aheae4embvb9bkgw.polandcentral-01.azurewebsites.net"
    linuxFxVersion: "PYTHON|3.12"

    Config settings:
        "name":                             "value"
        "SCM_DO_BUILD_DURING_DEPLOYMENT"    "true"
        "WEBSITE_RUN_FROM_PACKAGE"          "0"
        "PNM_BOT_TOKEN"                      "******"  //(is true for  "Pga News Monitor Bot")

Тестовая бизнес логика:

Пользователь постит сообщение в телеграм канал    -> 
    бот отпраляет его в сервис ->
    сервис получает его парменты обрабатывае  в pytho code -> 
    отправляет его боту ->
    бот отправляет в телеграм сообщение типа : mesage id:#### - processed

замечания по  DevOps:

    Код пишем локально в VS Code integrated with Git repo - https://github.com/peisakhovich/tb_v5
     
    В  AZURE service: "test-tb-001" деплою "вручную" не используя CI/CD опыт показывает так меньше проблем 
    с зависанием сбойных версий кода  и больше контроля. 