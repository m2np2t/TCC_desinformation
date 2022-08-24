import re

#text = "@verifato  fasjvbrah"

def treatentry (message):
    
    #é nescessário tratar mensagens com fechamento de aspas duplas interno por exemplo "asvbhbv"kajebvefb"bjnsj"
    expression = "@verifato"

    verify = message[0:9]
    qtd = len(message)

    if(verify == expression) and (qtd < 5000):

        messageWithSimpleQuotationMarks = "^\'.*\'$"
        messageWithDoubleQuotationMarks = "^\".*\"$"
        
        if re.match(expression, message):
            match = message
        message = message.replace(expression, "")
        message = message.strip()
        if re.match(messageWithSimpleQuotationMarks, message):
            message = message.strip("'")
        elif re.match(messageWithDoubleQuotationMarks, message):
            message = message.strip('"')

        return True
        
    
    else:

        text = "Sua análise não contem o @verifato antes da análise ou sua análise esta acima de 255 caracteres .por gentileza caso deseje analisar insira o termo @verifato e verifique o tamanho de sua análise"

        return False

#treatentry(text)
