# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import ctypes

OS = "Windows"
FASTIR_ROOT = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "."))

EXTRACT_DUMP = {
    "mft": "csv_mft",
    "dd": "csv_export_dd",
    "ram": "csv_export_ram",
    "rekall": "csv_rekall_cmd",
    "mbr": "csv_mbr"
}

FILTERS_MAGIC = {"application/msword",
                 "application/octet-stream",
                 "application/x-archive",
                 "application/x-dosexec",
                 "application/x-elc",
                 "application/x-executable, statically linked, stripped",
                 "application/x-gzip",
                 "application/x-object, not stripped",
                 "application/x-zip",
                 "image/bmp",
                 "image/gif",
                 "image/jpeg",
                 "image/png", "text/html",
                 "text/rtf",
                 "text/xml",
                 "UTF-8 Unicode HTML document text, with CRLF line terminators",
                 "UTF-8 Unicode HTML document text, with very long lines, with CRLF, LF line terminators"}
HASH_ALGO = "sha256"
VIRUS_TOTAL = "http://www.virustotal.com/en/file/%s/analysis"
NETWORK_ADAPTATER = {
    0: "Ethernet 802.3",
    1: "Token Ring 802.5",
    2: "Fiber Distributed Data Interface (FDDI)",
    3: "Wide Area Network (WAN)",
    4: "LocalTalk",
    5: "Ethernet using DIX header format",
    6: "ARCNET",
    7: "ARCNET (878.2)",
    8: "ATM",
    9: "Wireless",
    10: "Infrared Wireless",
    11: "Bpc",
    13: "CoWan",
    14: "1394",
    15: "Tunnel"
}

LONGLONGSIZE = ctypes.sizeof(ctypes.c_longlong)
BYTESIZE = ctypes.sizeof(ctypes.c_byte)
WORDSIZE = 2
DWORDSIZE = 4

USERS_FOLDER = {
    "Windows10": "C:\\Users",
    "Windows8": "C:\\Users",
    "Windows8_1": "C:\\Users",
    "Windows7": "C:\\Users",
    "Windows2012Server":"C:\\User",
    "Windows2012ServerR2":"C:\\User",
    "WindowsXP": "C:\\Users",
    "WindowsVista": "C:\\Users",
    "Windows2008ServerR2": "C:\\Users",
    "Windows2008Server": "C:\\Users",
    "WindowsXP": "C\Documents and Settings",
    "Windows2003Server": "C\Documents and Settings",
    "Windows2003ServerR2": "C\Documents and Settings"
}