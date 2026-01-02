import sys
import os
from PyQt6.QtWidgets import QApplication, QLabel, QMenu, QWidget, QMessageBox
from PyQt6.QtCore import Qt, QPoint, QSize
from PyQt6.QtGui import QMovie, QAction, QCursor

class GifWidget(QWidget):
    def __init__(self, gif_path):
        super().__init__()
        self.gif_path = gif_path
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.label = QLabel(self)
        self.movie = QMovie(self.gif_path)
        
        # Get original size
        self.movie.jumpToFrame(0)
        original_size = self.movie.currentImage().size()
        if original_size.isEmpty():
            self.base_size = QSize(200, 200)
        else:
            self.base_size = original_size

        self.label.setMovie(self.movie)
        self.setCursor(Qt.CursorShape.OpenHandCursor)
        
        # Default size
        self.current_scale = 0.5
        self.resize_gif(0.5)
        
        # Scroll enabled by default
        self.scroll_enabled = False
        
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)

    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None
        self.setCursor(Qt.CursorShape.OpenHandCursor)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        
        # Resize options
        resize_menu = menu.addMenu("Boyutu Değiştir")
        
        small_action = QAction("Küçük (%50)", self)
        small_action.triggered.connect(lambda: self.resize_gif(0.5))
        resize_menu.addAction(small_action)
        
        normal_action = QAction("Normal (%100)", self)
        normal_action.triggered.connect(lambda: self.resize_gif(1.0))
        resize_menu.addAction(normal_action)
        
        large_action = QAction("Büyük (%150)", self)
        large_action.triggered.connect(lambda: self.resize_gif(1.5))
        resize_menu.addAction(large_action)
        
        extra_large_action = QAction("Çok Büyük (%200)", self)
        extra_large_action.triggered.connect(lambda: self.resize_gif(2.0))
        resize_menu.addAction(extra_large_action)
        
        menu.addSeparator()
        
        scroll_toggle_action = QAction(f"Scroll ile Boyutlandırma ({'Açık' if self.scroll_enabled else 'Kapalı'})", self)
        scroll_toggle_action.triggered.connect(self.toggle_scroll)
        menu.addAction(scroll_toggle_action)
        
        menu.addSeparator()
        
        info_action = QAction("Info", self)
        info_action.triggered.connect(self.show_info)
        menu.addAction(info_action)
        
        menu.addSeparator()
        
        close_all_action = QAction("Tümünü Kapat", self)
        close_all_action.triggered.connect(self.close_all_widgets)
        menu.addAction(close_all_action)
        
        menu.addSeparator()
        
        kill_action = QAction("Kill (Uygulamayı Kapat)", self)
        kill_action.triggered.connect(self.kill_app)
        menu.addAction(kill_action)
        
        menu.addSeparator()
        
        close_action = QAction("Kapat", self)
        close_action.triggered.connect(self.close)
        menu.addAction(close_action)
        
        menu.exec(event.globalPos())
    
    def toggle_scroll(self):
        self.scroll_enabled = not self.scroll_enabled
    
    def kill_app(self):
        app = QApplication.instance()
        app.quit()
    
    def show_info(self):
        info_text = (
            "Giffa - GIF Görüntüleyici\n\n"
            "Kullanım:\n"
            "- GIF dosyalarınızı bu klasöre ekleyin:\n"
            "  C:\\Users\\USER\\Pictures\\gifs\n\n"
            "Özellikler:\n"
            "- Sol tık ve sürükle ile GIF'leri hareket ettirin\n"
            "- Sağ tık ile menüyü açın:\n"
            "  * Boyutu Değiştir: Ön tanımlı boyutlar\n"
            "  * Scroll ile Boyutlandırma: Mouse tekerleği ile boyutlandırma özelliğini aç/kapat\n"
            "  * Info: Bilgi ekranı\n"
            "  * Tümünü Kapat: Tüm GIF'leri kapatır\n"
            "  * Kill (Uygulamayı Kapat): Uygulamayı tamamen kapatır\n"
            "  * Kapat: Bu GIF'i kapatır\n"
        )
        QMessageBox.information(self, "Giffa Info", info_text)
    
    def close_all_widgets(self):
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, GifWidget):
                widget.close()
    
    def wheelEvent(self, event):
        if not self.scroll_enabled:
            return
        delta = event.angleDelta().y() / 120
        new_scale = self.current_scale + (delta * 0.1)
        new_scale = max(0.1, min(new_scale, 3.0))
        self.resize_gif(new_scale)

    def resize_gif(self, scale):
        self.current_scale = scale
        new_width = int(self.base_size.width() * scale)
        new_height = int(self.base_size.height() * scale)
        new_size = QSize(new_width, new_height)
        
        self.movie.setScaledSize(new_size)
        self.label.setFixedSize(new_size)
        self.setFixedSize(new_size)
        
        if self.movie.state() == QMovie.MovieState.NotRunning:
            self.movie.start()
        else:
            self.movie.stop()
            self.movie.start()

def main():
    app = QApplication(sys.argv)
    
    # Get screen geometry
    screen = app.primaryScreen().availableGeometry()
    screen_width = screen.width()
    screen_height = screen.height()
    
    gif_dir = r"C:\Users\USER\Pictures\gifs"
    if not os.path.exists(gif_dir):
        os.makedirs(gif_dir)
        QMessageBox.information(None, "Klasör Oluşturuldu", f"GIF klasörü oluşturuldu:\n{gif_dir}\n\nLütfen bu klasöre GIF dosyalarını ekleyiniz ve uygulamayı tekrar çalıştırınız.")
        return

    gifs = [f for f in os.listdir(gif_dir) if f.lower().endswith('.gif')]
    
    if not gifs:
        QMessageBox.warning(None, "GIF Bulunamadı", f"Klasörde GIF dosyası bulunamadı:\n{gif_dir}\n\nLütfen bu klasöre GIF dosyalarını ekleyiniz ve uygulamayı tekrar çalıştırınız.")
        return

    widgets = []
    
    margin = 10
    current_x = screen_width
    current_y = margin
    column_width = 0
    
    # Create widgets first to know their sizes
    for gif_name in gifs:
        gif_path = os.path.join(gif_dir, gif_name)
        widget = GifWidget(gif_path)
        widgets.append(widget)

    # Initial column setup
    current_column_widgets = []
    
    # Simple 2-column layout logic starting from right
    col_index = 0
    row_index = 0
    
    # We want to place them in 2 columns on the right
    # Let's calculate positions
    
    # Group into pairs for "2-li üst üste"
    # Actually "2-li" usually means 2 columns. 
    # User said "sağ tarafına 2 li üst üste dizilsinler" 
    # This likely means 2 columns, starting from the right.
    
    x_offset = screen_width
    y_offset = margin
    max_w_in_col = 0
    
    col_count = 2
    padding = 10
    
    # To properly align from right, we need to know the widths
    # Let's group them into columns of 2 widgets each horizontally? 
    # Or 2 columns of many widgets vertically? 
    # "2 li üst üste" usually means 2 columns of widgets.
    
    # Correct interpretation: 2 columns, starting from far right.
    # Column 1 (far right), Column 2 (to the left of Column 1).
    
    # First, let's determine the width of each column (max width of widgets in that column)
    # But since they are all %50, we can just place them.
    
    # Let's use a simpler approach:
    # Col 0: Rightmost
    # Col 1: Left of Col 0
    
    cols = [[], []]
    for i, w in enumerate(widgets):
        cols[i % 2].append(w)
        
    # Now position them
    current_right = screen_width - margin
    
    for col in range(2):
        max_w = 0
        if not cols[col]: continue
        
        # Find max width in this column
        for w in cols[col]:
            max_w = max(max_w, w.width())
            
        current_x = current_right - max_w
        current_y = margin
        
        for w in cols[col]:
            # Check if it fits vertically
            if current_y + w.height() > screen_height - margin:
                # If it doesn't fit, this simple layout logic needs to shift left
                # But the user said "sığmazsa sola kaysın"
                # This means we start a new pair of columns to the left
                pass # We'll refine this in a more robust loop below
            
            w.move(current_x, current_y)
            current_y += w.height() + margin
            
        current_right = current_x - margin

    # Robust layouting:
    # We fill 2 columns at a time, moving left if we hit the bottom.
    
    current_x_right_boundary = screen_width - margin
    current_y = margin
    col_widths = [0, 0] # widths of the 2 current columns
    
    # Reset positions for robust calculation
    current_y = [margin, margin] # Y positions for col 0 and col 1
    current_x_base = screen_width - margin
    
    # We'll place them one by one, alternating columns
    # If a column exceeds height, we shift the "base" X to the left and reset Y
    
    for i, w in enumerate(widgets):
        col_idx = i % 2
        
        # If this widget would go off screen bottom
        if current_y[col_idx] + w.height() > screen_height - margin:
            # Shift everything left
            # The new base X will be the leftmost point of the current 2 columns
            shift = max(col_widths) + margin
            current_x_base -= (shift * 2) # move back for next set of 2 columns
            current_y = [margin, margin]
            col_widths = [0, 0]
            
        # Update column width
        col_widths[col_idx] = max(col_widths[col_idx], w.width())
        
        # Calculate X: 
        # Col 0 is rightmost: base_x - width
        # Col 1 is to the left: base_x - col0_width - margin - width
        if col_idx == 0:
            target_x = current_x_base - w.width()
        else:
            target_x = current_x_base - col_widths[0] - margin - w.width()
            
        w.move(target_x, current_y[col_idx])
        current_y[col_idx] += w.height() + margin
        w.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
