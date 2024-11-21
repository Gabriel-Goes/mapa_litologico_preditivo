import geopandas as gpd
import fiona

# Definindo caminho
def gdb(path=''):
    '''
    Diretório raíz dos dados : '/home/ggrl/geodatabase/'

        path : caminho até o arquivo desejado
    '''
    gdb = '/home/ggrl/geodatabase/' + path
    return gdb


# IMPORTADOR DE LITOLOGIAS POR ESCALA --------------------------------------------------------------------------#
def importar_geometrias(camada, mapa=False):
    '''
    Recebe:
        camada      : camada vetorial a ser lida do geopackage.
        mapa        : nome do mapa presente na camada vetorial;

    Retorna:
        Objeto GeoDataFrame.
        
    Se houver seleçao de mapa retornara apenas as geometrias que possuem o nome escolhido na coluna ['MAPA']
    Se Retornar camada vazia recebera a lista das camadas veotoriais diposniveis
    Se mapa == False: retorna todos os objetos presente nesta camada vetorial
    '''
   
    try:
        lito =  gpd.read_file(gdb('geodatabase.gpkg'),
                              driver= 'GPKG',
                              layer= camada)
    except ValueError:
        print(f"# -- Lista de camadas vetoriais disponívei: {fiona.listlayers(gdb('geodatabase.gpkg'))}")

    if mapa:
        folha = lito[lito.MAPA == 'Carta geológica da folha ' + mapa]             # df[df.series]
        
        if folha.empty:

            print("# O mapa escolhido nao está presente na coluna MAPA da camada veotiral. Os mapas disponiveis serao listados a seguir.")
            print(" ")
            print('# Digite apenas o nome do mapa após <Carta geológica da folha>. (SEM ESPAÇO)')
            print(" ")
            print(f"# -- Lista de mapas: {list(lito.MAPA.unique())}")

            lista_mapas = list(lito.MAPA.unique())
            return lista_mapas

        else:    
            return(folha)


    else:
        return(lito)