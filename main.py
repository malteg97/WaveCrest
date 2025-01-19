import GUI
import save_data as save
import threading


# Hauptprogramm
GUI.init_GUI()

saving = threading.Thread(target=save.periodic_save, daemon=True)
saving.start()

GUI.update_GUI()
GUI.root.mainloop()
