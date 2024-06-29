import subprocess
import xbmc
import xbmcgui

def run_steamlink():
    try:
        xbmcgui.Dialog().notification('SteamLink Launcher', 'Lanzando SteamLink...', xbmcgui.NOTIFICATION_INFO, 5000)
        result = subprocess.run(['flatpak', 'run', 'com.valvesoftware.SteamLink'], check=True)
        if result.returncode == 0:
            xbmcgui.Dialog().notification('SteamLink Launcher', 'SteamLink se ejecutó correctamente', xbmcgui.NOTIFICATION_INFO, 5000)
        else:
            xbmcgui.Dialog().notification('SteamLink Launcher', 'Error al ejecutar SteamLink', xbmcgui.NOTIFICATION_ERROR, 5000)
    except subprocess.CalledProcessError as e:
        xbmcgui.Dialog().notification('SteamLink Launcher', f'Error: {e}', xbmcgui.NOTIFICATION_ERROR, 5000)
    except Exception as e:
        xbmcgui.Dialog().notification('SteamLink Launcher', f'Excepción: {e}', xbmcgui.NOTIFICATION_ERROR, 5000)

if __name__ == '__main__':
    run_steamlink()
