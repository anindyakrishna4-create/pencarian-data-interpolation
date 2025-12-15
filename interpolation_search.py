# File: interpolation_search.py (Logika Algoritma)

# List global untuk menyimpan riwayat langkah
HISTORY = []

def interpolation_search(data_list, target):
    """
    Mengimplementasikan Interpolation Search dan mencatat setiap langkah di HISTORY.
    Mengembalikan index jika ditemukan, atau -1 jika tidak ditemukan.
    """
    global HISTORY
    HISTORY = []
    
    # Prasyarat: Array harus terurut! Kita asumsikan array input sudah terurut.
    arr = sorted(data_list[:]) 
    n = len(arr)
    low = 0
    high = n - 1
    found_index = -1
    
    # Catat status awal
    HISTORY.append({
        'array': arr[:],
        'target': target,
        'low': low, 
        'high': high,
        'pos': -1, 
        'status': 'Mulai',
        'action': f'Memulai Interpolation Search untuk nilai {target}. Array harus TERURUT.'
    })

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Jika low dan high sama, cek apakah target adalah nilai tersebut
        if low == high:
            if arr[low] == target:
                found_index = low
                break
            else:
                break # Target tidak ada
        
        # --- Formula Interpolasi untuk memprediksi posisi (pos) ---
        try:
            # Formula di atas, dikonversi ke integer untuk indeks
            pos = int(low + ((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))
        except ZeroDivisionError:
             # Jika arr[high] == arr[low], artinya semua elemen di rentang sama.
             # Cek low saja, lalu keluar loop jika tidak cocok.
             pos = low
        
        # Batasi pos agar tidak keluar dari rentang low dan high
        pos = max(low, min(high, pos)) 
        
        # Catat langkah pengecekan
        HISTORY.append({
            'array': arr[:],
            'target': target,
            'low': low, 
            'high': high,
            'pos': pos,
            'status': 'Prediksi',
            'action': f'Menggunakan formula interpolasi, memprediksi posisi (pos) di Indeks {pos}. Nilai: {arr[pos]}. Rentang: [{low} - {high}]'
        })
        
        if arr[pos] == target:
            found_index = pos
            # Catat langkah Ditemukan
            HISTORY.append({
                'array': arr[:],
                'target': target,
                'low': low, 
                'high': high,
                'pos': pos,
                'status': 'Ditemukan',
                'action': f'Nilai {target} DITEMUKAN pada Indeks {pos}!'
            })
            break
            
        elif arr[pos] < target:
            # Target ada di sebelah kanan, buang sebelah kiri (low = pos + 1)
            low = pos + 1
            HISTORY.append({
                'array': arr[:],
                'target': target,
                'low': low, 
                'high': high,
                'pos': pos,
                'status': 'Pindah Kanan',
                'action': f'Nilai terlalu kecil. Pindahkan batas Bawah (low) ke {low}.'
            })
            
        else: # arr[pos] > target
            # Target ada di sebelah kiri, buang sebelah kanan (high = pos - 1)
            high = pos - 1
            HISTORY.append({
                'array': arr[:],
                'target': target,
                'low': low, 
                'high': high,
                'pos': pos,
                'status': 'Pindah Kiri',
                'action': f'Nilai terlalu besar. Pindahkan batas Atas (high) ke {high}.'
            })

    # Catat status selesai (HANYA jika loop berakhir)
    if found_index == -1:
        HISTORY.append({
            'array': arr[:],
            'target': target,
            'low': low, 
            'high': high,
            'pos': -1,
            'status': 'Selesai',
            'action': f'Selesai. Target tidak berada di rentang [low - high]. Nilai {target} tidak ditemukan.'
        })
        
    return found_index, HISTORY
