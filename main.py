import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import gc

import header as h

source_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/4_LLR_DATA_SEGMENTATION/" \
                "NPZ_FILES_BY_TARGET"
f_graph_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/6_LLR_FREQ_GRAPHS/" \
                "FFT_FORCE"
v_graph_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/6_LLR_FREQ_GRAPHS/" \
                "FFT_VELOCITY"
df_graph_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/6_LLR_FREQ_GRAPHS/" \
                  "FFT_dFORCE"
dv_graph_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/6_LLR_FREQ_GRAPHS/" \
                  "FFT_dVELOCITY"
fa_graph_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/6_LLR_FREQ_GRAPHS/" \
                  "FFT_FORCE-ANGLE"
va_graph_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/6_LLR_FREQ_GRAPHS/" \
                  "FFT_VELOCITY-ANGLE"
dfa_graph_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/6_LLR_FREQ_GRAPHS/" \
                  "FFT_dFORCE-ANGLE"
dva_graph_folder = "D:/PD_Participant_Data/LLR_DATA_ANALYSIS_CLEANED/LLR_DATA_PROCESSING_PIPELINE/6_LLR_FREQ_GRAPHS/" \
                  "FFT_dVELOCITY-ANGLE"

# A - dFxy_Mag | B - dVxy_Mag | C - Fxy_Angle_Smooth | D - Vxy_Angle_Smooth | E - dFxy_Angle_Smooth | F - dVxy_Angle_Smooth


# Some variables to control what graphs save and which don't.
f_graph = False
v_graph = False
df_graph = True
dv_graph = True
fa_graph = True
va_graph = True
dfa_graph = True
dva_graph = True
save_graphs = True


# Define some constants.
freq = 100
rel_freq = 15
rel_freq_2 = 5

if __name__ == '__main__':
    print("Running frequency analysis...")
    if save_graphs:
        matplotlib.use('Agg')
        print(" File_name, orig_cc_x, new_cc_x, orig_cc_y, new_cc_y")
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
                if f_graph:
                    signal = np.asarray(target_list[:, h.data_header.index("Fxy_Mag")]).astype(float)
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
                    ax1.set_title("Absolute FFT of Force Magnitude Profile for Sample " + file_name)
                    save_str = f_graph_folder + '/' + file_name
                    if save_graphs:
                        plt.savefig(fname=save_str)
                        fig.clf()
                        gc.collect()
                    else:
                        plt.show()
                        plt.close()
                if v_graph:
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
                    save_str = v_graph_folder + '/' + file_name
                    if save_graphs:
                        plt.savefig(fname=save_str)
                        fig.clf()
                        gc.collect()
                    else:
                        plt.show()
                        plt.close()
                if dfa_graph:
                    signal = np.asarray(target_list[:, h.data_header.index("dFxy_Mag")]).astype(float)
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
                    ax1.set_title("Absolute FFT of Force Derivative Profile for Sample " + file_name)
                    save_str = df_graph_folder + '/' + file_name
                    if save_graphs:
                        plt.savefig(fname=save_str)
                        fig.clf()
                        gc.collect()
                    else:
                        plt.show()
                        plt.close()
                if dva_graph:
                    signal = np.asarray(target_list[:, h.data_header.index("dVxy_Mag")]).astype(float)
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
                    ax1.set_title("Absolute FFT of Velocity Derivative Profile for Sample " + file_name)
                    save_str = dv_graph_folder + '/' + file_name
                    if save_graphs:
                        plt.savefig(fname=save_str)
                        fig.clf()
                        gc.collect()
                    else:
                        plt.show()
                        plt.close()
                if fa_graph:
                    signal = np.asarray(target_list[:, h.data_header.index("Fxy_Angle_Smooth")]).astype(float)
                    f, fft = h.freq_analysis(signal, freq)
                    # Find value for relevant frequency.
                    rel_freq_ind = f[(f < rel_freq_2)]
                    # Plotting of data here.
                    fig = plt.figure(num=1, dpi=100, facecolor='w', edgecolor='w')
                    fig.set_size_inches(25, 8)
                    ax1 = fig.add_subplot(111)
                    ax1.plot(rel_freq_ind, fft[:rel_freq_ind.shape[0]], label="FFT for relevant frequencies")
                    # Set some labels.
                    file_name = file.split('.')[0]
                    ax1.set_xlabel("Frequency (Hz)")
                    ax1.set_ylabel("Amplitude (g/Hz)")
                    ax1.set_title("Absolute FFT of Force Angle Profile for Sample " + file_name)
                    save_str = fa_graph_folder + '/' + file_name
                    if save_graphs:
                        plt.savefig(fname=save_str)
                        fig.clf()
                        gc.collect()
                    else:
                        plt.show()
                        plt.close()
                if va_graph:
                    signal = np.asarray(target_list[:, h.data_header.index("Vxy_Angle_Smooth")]).astype(float)
                    f, fft = h.freq_analysis(signal, freq)
                    # Find value for relevant frequency.
                    rel_freq_ind = f[(f < rel_freq_2)]
                    # Plotting of data here.
                    fig = plt.figure(num=1, dpi=100, facecolor='w', edgecolor='w')
                    fig.set_size_inches(25, 8)
                    ax1 = fig.add_subplot(111)
                    ax1.plot(rel_freq_ind, fft[:rel_freq_ind.shape[0]], label="FFT for relevant frequencies")
                    # Set some labels.
                    file_name = file.split('.')[0]
                    ax1.set_xlabel("Frequency (Hz)")
                    ax1.set_ylabel("Amplitude (g/Hz)")
                    ax1.set_title("Absolute FFT of Velocity Angle Profile for Sample " + file_name)
                    save_str = va_graph_folder + '/' + file_name
                    if save_graphs:
                        plt.savefig(fname=save_str)
                        fig.clf()
                        gc.collect()
                    else:
                        plt.show()
                        plt.close()
                if dfa_graph:
                    signal = np.asarray(target_list[:, h.data_header.index("dFxy_Angle_Smooth")]).astype(float)
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
                    ax1.set_title("Absolute FFT of Force Angle Derivative Profile for Sample " + file_name)
                    save_str = dfa_graph_folder + '/' + file_name
                    if save_graphs:
                        plt.savefig(fname=save_str)
                        fig.clf()
                        gc.collect()
                    else:
                        plt.show()
                        plt.close()
                if dva_graph:
                    signal = np.asarray(target_list[:, h.data_header.index("dFxy_Angle_Smooth")]).astype(float)
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
                    ax1.set_title("Absolute FFT of Velocity Angle Derivative Profile for Sample " + file_name)
                    save_str = dva_graph_folder + '/' + file_name
                    if save_graphs:
                        plt.savefig(fname=save_str)
                        fig.clf()
                        gc.collect()
                    else:
                        plt.show()
                        plt.close()
