import pytubefix
import streamlit as st

class YoutubeDownloader:
    def __init__(self, url):
        self.url = url
        self.youtube = pytubefix.YouTube(self.url, on_progress_callback=YoutubeDownloader.onProgress)
        self.stream = None

    def showStreams(self):
        streams = self.youtube.streams
        stream_options = [
            f"Resolución: {stream.resolution or 'N/A'} / FPS: {getattr(stream, 'fps', 'N/A')} / Tipo: {stream.mime_type}"
            for stream in streams
        ]
        choice = st.selectbox("Elija una opción de stream:", stream_options)
        self.stream = streams[stream_options.index(choice)]

    def showTitle(self):
        st.write(f"**Título:** {self.youtube.title}")
        self.showStreams()

    def getFileSize(self):
        if self.stream:
            file_size = self.stream.filesize / 1000000
            return file_size
        return 0

    def getPermissionToContinue(self, file_size):
        st.write(f"**Título:** {self.youtube.title}")
        st.write(f"**Autor:** {self.youtube.author}")
        st.write(f"**Tamaño:** {file_size:.2f}MB")
        st.write(f"**Resolución:** {self.stream.resolution or 'N/A'}")
        st.write(f"**FPS:** {getattr(self.stream, 'fps', 'N/A')}")

        if st.button("Descargar"):
            self.download()

    def download(self):
        if self.stream:
            self.stream.download()
            st.success("¡Descarga Completada!")
        else:
            st.error("No se ha seleccionado un stream válido.")

    @staticmethod
    def onProgress(stream=None, chunk=None, remaining=None):
        if stream:
            file_size = stream.filesize / 1000000
            file_download = file_size - (remaining / 1000000)
            st.progress(file_download / file_size)

if __name__ == "__main__":
    st.title("Descargador de Videos de YT")
    url = st.text_input("Ingrese la URL del video:")

    if url:
        downloader = YoutubeDownloader(url)
        downloader.showTitle()
        if downloader.stream:
            file_size = downloader.getFileSize()
            downloader.getPermissionToContinue(file_size)
