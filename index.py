import matplotlib.pyplot as plt
import pandas as pd

#data_frame = {'eixo X': [16, 256, 361, 484],'eixo Y': [9, 441, 900, 784]}
# --------------------------------------------------------------- *** Plot *** ---------------------------------------------------------------
#plt.plot(data_frame['eixo X'], data_frame['eixo Y'], label='Datas', color='#296073', lw=0.4)
#plt.xlabel(xlabel='Eixo X')
#plt.ylabel(ylabel='Eixo Y')
#plt.title(label='Graphic title')
#plt.legend()

# -------------------------------------------------------------- *** Scatter *** -------------------------------------------------------------
#plt.scatter(x=data_frame['eixo X'], y=data_frame['eixo Y'], color='#845EC2')

# --------------------------------------------------------------- *** Bar *** ---------------------------------------------------------------
#plt.bar(data_frame['eixo X'], data_frame['eixo Y'], color='#3596B5')


#plt.plot(data_frame['eixo X'], data_frame['eixo Y'], label='Datas', color='#296073', lw=0.4)
#plt.axis(xmin=0, xmax=1000, ymin=0, ymax=1000)


#figura = plt.figure(figsize=(16,9))
#figura.suptitle(t='Test title')

#figura.add_subplot(131)
#plt.plot(data_frame['eixo X'], data_frame['eixo Y'])
#plt.legend()
#plt.title('Gráfico 1')

#figura.add_subplot(133)
#plt.scatter(data_frame['eixo X'], data_frame['eixo Y'])
#plt.title('Gráfico 2')

#figura.add_subplot(132)
#plt.bar(data_frame['eixo X'], data_frame['eixo Y'])
#plt.title('Gráfico 3')

#plt.savefig('Graficos.png')

table = 'indexData.csv'
cotacao_df = pd.read_csv(table)

cotacao_df1 = cotacao_df[['Index', 'Date', 'Close']]
df_remove = cotacao_df1.loc[(cotacao_df1['Index'] != 'NYA')]
cotacao_df_final = cotacao_df1.drop(df_remove.index)
cotacao_df_final = cotacao_df_final[13900:]

plt.plot(cotacao_df_final['Date'], cotacao_df_final['Close'], label='NYA', color='#296073', lw='0.8')
plt.xlabel(xlabel='Data da cotação')
plt.ylabel(ylabel='Valor do fechamento')
plt.legend()
plt.title(label='Gráfico de cotação da Bolsa de New York')

plt.show()