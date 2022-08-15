import os
import numpy as np
import matplotlib.pyplot as plt
import gc

import header as h

source_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/4_LLR_DATA_SEGMENTATION/" \
                "NPZ_FILES_BY_TARGET"
storage_name = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/6_LLR_FREQ_GRAPHS/" \
                "FFT_VELOCITY"
freq = 100
rel_freq = 15

if __name__ == '__main__':
    print("Running frequency analysis...")
    for file in os.listdir(source_folder):
        if file.endswith('.npz'):
            task_number = h.get_task_number(file)
            if (("T1" in file) or ("T2" in file)) & ("V0" in file):
                # Here if file includes task 1 and 2, and if it also is a V0 file, as I'm not studying other pieces
                # of information.
                print(file)
                source_file = source_folder + '/' + file
                # The source file is a npz file. So I need to load in the data and unpack.
                data = np.load(source_file, allow_pickle=True)
                # Unpack the data.
                ragged_list, target_list, target_i = h.load_npz(data)
                signal = np.asarray(target_list[:, h.data_header.index("Vxy_Mag")]).astype(float)
                f, fft = h.freq_analysis(signal, freq)
                # Find value for relevant frequency.
                rel_freq_ind = f[(f < rel_freq)]
                # Plotting of data here.
                fig = plt.figure(num=1, dpi=100, facecolor='w', edgecolor='w')
                fig.set_size_inches(25, 8)
                ax1 = fig.add_subplot(111)
                ax1.plot(rel_freq_ind, fft[:rel_freq_ind.shape[0]], label="FFT for relevant frequencies")
                # Set some labels.
                file_name = file.split('.')[0]
                ax1.set_xlabel("Frequency (Hz)")
                ax1.set_ylabel("Amplitude (g/Hz)")
                ax1.set_title("Absolute FFT of Velocity Magnitude Profile for Sample " + file_name)
                save_str = storage_name + '/' + file_name
                plt.savefig(fname=save_str)
                fig.clf()
                gc.collect()
