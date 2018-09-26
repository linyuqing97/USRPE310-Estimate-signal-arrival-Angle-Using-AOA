#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Master
# Generated: Sat Sep 15 09:54:10 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import doa
import sip
import sys
import xmlrpclib


class master(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Master")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Master")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "master")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.n_points = n_points = 5000
        self.downsample = downsample = 50
        self.transition = transition = 2e5
        self.slope_samples = slope_samples = 100
        self.samp_rate1 = samp_rate1 = 48000
        self.samp_rate = samp_rate = 1e6
        self.rx_gain = rx_gain = 50
        self.rtl_samp_rate = rtl_samp_rate = 1e6
        self.pi = pi = 3.1415926535
        self.freq_correction_default = freq_correction_default = -0.16
        self.freq = freq = 2.1e9
        self.down_width = down_width = n_points/downsample
        self.cutoff = cutoff = 1e5
        self.calibrate = calibrate = 1
        self.c = c = 299792458
        self.audio_gain = audio_gain = 0.5

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Aligned DOA')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'X-Corr')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Messages')
        self.top_layout.addWidget(self.tab)
        self._freq_range = Range(80e6, 2.2e9, 100e3, 2.1e9, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency (Hz)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 0,0,1,2)
        self._audio_gain_range = Range(0, 1, 0.1, 0.5, 100)
        self._audio_gain_win = RangeWidget(self._audio_gain_range, self.set_audio_gain, 'Audio Gain', "counter_slider", float)
        self.top_layout.addWidget(self._audio_gain_win)
        self.zeromq_pull_source_0_1 = zeromq.pull_source(gr.sizeof_float, 1, 'tcp://10.42.0.51:9997', 100, False, -1)
        self.zeromq_pull_source_0_0_0 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://10.42.0.51:9998', 100, False, -1)
        self.zeromq_pull_source_0_0 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://10.42.0.51:9992', 10000, False, -1)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://10.42.0.51:9991', 10000, False, -1)
        self.xmlrpc_client0 = xmlrpclib.Server('http://10.42.0.51:30000')
        self.xmlrpc_client = xmlrpclib.Server('http://10.42.0.51:30000')
        self._rx_gain_range = Range(0, 70, 1, 50, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RF Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 1,0,1,2)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	409, #samp_rate
        	"Capon DOA Angle", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-3.2, 3.2)
        
        self.qtgui_time_sink_x_0.set_y_label('Angle', "radians")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 3,0,1,3)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.01)
        self.qtgui_number_sink_0.set_title("Degree")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -180)
            self.qtgui_number_sink_0.set_max(i, 180)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	1e6, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_edit_box_msg_0_1 = qtgui.edit_box_msg(qtgui.STRING, 'reset_buffer', 'Reset Alignment Buffer', False, False, 'recalc')
        self._qtgui_edit_box_msg_0_1_win = sip.wrapinstance(self.qtgui_edit_box_msg_0_1.pyqwidget(), Qt.QWidget)
        self.tab_layout_2.addWidget(self._qtgui_edit_box_msg_0_1_win)
        self.qtgui_edit_box_msg_0_0 = qtgui.edit_box_msg(qtgui.FLOAT, '0', 'Reset Sample Drift Correction', True, False, 'reset_sum')
        self._qtgui_edit_box_msg_0_0_win = sip.wrapinstance(self.qtgui_edit_box_msg_0_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_2.addWidget(self._qtgui_edit_box_msg_0_0_win)
        self.doa_capon_ccf_0_0 = doa.capon_ccf(down_width)
        _calibrate_check_box = Qt.QCheckBox('Enable Calibration')
        self._calibrate_choices = {True: 1, False: 0}
        self._calibrate_choices_inv = dict((v,k) for k,v in self._calibrate_choices.iteritems())
        self._calibrate_callback = lambda i: Qt.QMetaObject.invokeMethod(_calibrate_check_box, "setChecked", Qt.Q_ARG("bool", self._calibrate_choices_inv[i]))
        self._calibrate_callback(self.calibrate)
        _calibrate_check_box.stateChanged.connect(lambda i: self.set_calibrate(self._calibrate_choices[bool(i)]))
        self.top_layout.addWidget(_calibrate_check_box)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, down_width)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, down_width)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vff((180/pi, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((audio_gain, ))
        self.blocks_keep_one_in_n_3 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 50)
        self.blocks_keep_one_in_n_2 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 50)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1, '/home/coding/Desktop/5', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.audio_sink_0 = audio.sink(48000, '', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_keep_one_in_n_2, 0), (self.blocks_stream_to_vector_0_1, 0))    
        self.connect((self.blocks_keep_one_in_n_3, 0), (self.blocks_stream_to_vector_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.doa_capon_ccf_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.doa_capon_ccf_0_0, 1))    
        self.connect((self.doa_capon_ccf_0_0, 0), (self.blocks_file_sink_1, 0))    
        self.connect((self.doa_capon_ccf_0_0, 0), (self.blocks_multiply_const_vxx_3, 0))    
        self.connect((self.doa_capon_ccf_0_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.zeromq_pull_source_0, 0), (self.blocks_keep_one_in_n_3, 0))    
        self.connect((self.zeromq_pull_source_0_0, 0), (self.blocks_keep_one_in_n_2, 0))    
        self.connect((self.zeromq_pull_source_0_0_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.zeromq_pull_source_0_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "master")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_n_points(self):
        return self.n_points

    def set_n_points(self, n_points):
        self.n_points = n_points
        self.set_down_width(self.n_points/self.downsample)

    def get_downsample(self):
        return self.downsample

    def set_downsample(self, downsample):
        self.downsample = downsample
        self.set_down_width(self.n_points/self.downsample)

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition

    def get_slope_samples(self):
        return self.slope_samples

    def set_slope_samples(self, slope_samples):
        self.slope_samples = slope_samples

    def get_samp_rate1(self):
        return self.samp_rate1

    def set_samp_rate1(self, samp_rate1):
        self.samp_rate1 = samp_rate1

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.xmlrpc_client0.set_rx_gain(self.rx_gain)

    def get_rtl_samp_rate(self):
        return self.rtl_samp_rate

    def set_rtl_samp_rate(self, rtl_samp_rate):
        self.rtl_samp_rate = rtl_samp_rate

    def get_pi(self):
        return self.pi

    def set_pi(self, pi):
        self.pi = pi
        self.blocks_multiply_const_vxx_3.set_k((180/self.pi, ))

    def get_freq_correction_default(self):
        return self.freq_correction_default

    def set_freq_correction_default(self, freq_correction_default):
        self.freq_correction_default = freq_correction_default

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.xmlrpc_client.set_freq(self.freq)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, 1e6)

    def get_down_width(self):
        return self.down_width

    def set_down_width(self, down_width):
        self.down_width = down_width

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff

    def get_calibrate(self):
        return self.calibrate

    def set_calibrate(self, calibrate):
        self.calibrate = calibrate
        self._calibrate_callback(self.calibrate)

    def get_c(self):
        return self.c

    def set_c(self, c):
        self.c = c

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self.blocks_multiply_const_vxx_0_0.set_k((self.audio_gain, ))


def main(top_block_cls=master, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
