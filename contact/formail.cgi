#! /usr/bin/perl

;# �� Perl�����n�̃p�X���w��B�s���ȏꍇ�̓v���o�C�_���T�[�o�[�Ǘ��҂Ɋm�F�B

;#   <iMODE/J-SKY�Ή�> �t�H�[�����[�� [�t�H�[���[�� SE] 
;#    - Version 3.03 / Jul 27, 2004
;#    - Copyright(C)2004 WEB POWER. All Rights Reserved.
;#    - �ŐV�ŁE�ŐV���� <http://www-power.net/>

Show_File_by_CGI($1) if ($ENV{'QUERY_STRING'} =~ /^\[(\w+)\]$/);
#BEGIN_INIT
#-----------------------------------------------------------------------------#
# �������珉���ݒ�ł��i�T�[�o�[�ւ̐ݒu���@�͓����̃}�j���A���������������j  #
#-----------------------------------------------------------------------------#
#
# <<���ӎ���>>
#  * �����ȊO��''���ɋL�q���܂��B'����ꂽ���ꍇ�� ����'�� \'�ɂ��Ă��������B
#      ex) �~ $var = value;  ��  �� $var = 'value';
#      ex) �~ $var = 'I can't';  ��  �� $var = 'I can\'t';
#  * $ # ; ' ���̋L���͊Ԉ���ď����Ȃ��悤�ɒ��ӂ��Ă��������B
#  * 1�����̃~�X�ł��v���O�����͓����܂���B�ݒ�E�ҏW�͐T�d�ɂ��܂��傤�B
#  * �s�̓���"#"��t����ƁA���̍s�͖����ɂȂ�܂��B(�R�����g�A�E�g)
#  * �l��ݒ肵�Ȃ��ꍇ�́A''���R�����g�A�E�g���Ă��������B
#      ex) �~ $var = ;  ��  �� $var = '';
#  * �����ݒ�ȊO�̕�����1�o�C�g�ł��ύX�����ꍇ�̓���ۏ؂͈�؂��܂���B
#  * �ڂ����͖{�T�C�g�̉��/FAQ�����Q�Ƃ��Ă��������B
#  * �����R�[�h�͎����F���ł����A�g�ѓd�b�Ŏg���ꍇ��"SHIFT_JIS"��p�ł��B


#=> ���[���̑��M����Œ肷��ꍇ�͂��̃A�h���X���w�肵�Ă��������B
#  * �����Ŏw�肷��ƁA���M�҂ɑ��M�����T�����[���������āA���̃A�h���X�ȊO
#    �ɂ͑��M���܂���B�t�H�[�������"_mailto"�͖�������܂��B
#  * (�d�v)�e�X�g���M����ꍇ�ł��K�����݂���L���ȃA�h���X(������)�ɂ��Ă���
#    �����B�K���ȃA�h���X�ɑ��M����ƁA�֌W�̂Ȃ����Ƀ��[�����͂�����A�G���[
#    ���[���̔����ɂ���O�҂ɖ��f��������܂��B
$INI{'mailto'} = 'shiina@zenta1.com';

#=> �t�@�C���A�b�v���[�h������ (1:����^0:���Ȃ�)
#  * �����Ȃ��ꍇ�A�}���`�p�[�g�t�H�[���f�[�^�����M����Ă��G���[��Ԃ��܂��B
#  * ���N�G�X�g���\�b�h��'GET'�̏ꍇ�͎g���܂���B
$SYS{'UseMultipart'} = 0;

#=> POST���\�b�h�Ŏ󂯎��ő�e��[�L���o�C�g]
#  * �T�[�o�[�A�N���C�A���g���Ή����Ă���΃v���O�����I�ɂ͏���͂���܂���B
#  * �T�[�o�[���ւ̕��ׂ��l�����āA���܂�傫�����Ȃ��悤�ɂ��Ă��������B
$SYS{'maxsize'} = 1024;#�L���o�C�g


#=> �^�C���]�[��
#  * GMT(�O���j�b�W�W����=�p�������h��)�Ƃ̎��� (���{��9����)
$INI{'TimeZone'} = 9;


#---<�p�X/URL�̐ݒ�>-----------------------------------------------------------
#
#   * �p�X�AURL�͂��ׂĔ��p�Ŏw�肵�Ă��������B(�S�p�͈�؎g���܂���)
#   * [�p�X]�Ƃ̓T�[�o�[���ł̏ꏊ�ł��Bhttp://�Ŏn�܂�URL�Ƃ͈Ⴄ���̂ł��B
#   * ���΃p�X�Ƃ̓X�N���v�g�̏ꏊ����Ƃ����p�X�̎w��ł��B
#      ../ => 1��̃f�B���N�g��  ./ => �����f�B���N�g��
#   * ��΃p�X�Ƃ̓T�[�o�[���̈�ԏ�̃f�B���N�g������Ƃ����p�X�̎w��ł��B
#       /usr/lib/sendmail  /home/foo/public_html/cgi-bin/script.cgi
#   * ���z�A�h���X�Ƃ�URL�̈ꕔ��(�h���C�����ȍ~)���w���܂��B
#       http://www.domain.com/~foo/cgi-bin/script.cgi
#                            ^ �h���C�����̌�̃X���b�V��"/"�ȍ~�̕���
#                              (/~foo/cgi-bin/script.cgi �̂���)


#=> ���C�u����(stdio.pl)��[�p�X]
$SYS{'stdiopl'}  = 'stdio.pl';

#=> ���C�u����(jcode.pl)��[�p�X]
$SYS{'jcodepl'}  = 'jcode.pl';

#=> ���[�����M�R�}���h(sendmail)��[�p�X]
$SYS{'sendmail'} = '/usr/sbin/sendmail';

#=> �e���|�����t�@�C���p�f�B���N�g����[�p�X]
#  * ���̃f�B���N�g���̃p�[�~�b�V������[777]�ɂ���B
$SYS{'TempDir'} = 'tmp/';

#=> ���M�Ҍ����Y�t�t�@�C���i�[�f�B���N�g����[�p�X]
#  * ���M�҈��Ƀt�@�C����Y�t�������[���𑗐M����ꍇ�A���̓Y�t�t�@�C��������f
#    �B���N�g���̃p�X���w�肵�܂��B
#  * ���M�҂���t�@�C�����A�b�v���[�h���Ă��炤�����̏ꍇ�͐ݒ�s�v�ł��B
$SYS{'FileDir'} = 'file/';

#=> �f�[�^�f�B���N�g���̃p�X
#  * ���̃f�B���N�g���̃p�[�~�b�V������[777]�ɂ���B
$SYS{'DataDir'} = 'data/';

#=> �f�[�^�t�@�C����URL(���̃p�X��http://�Ŏw��)
$SYS{'DataDirURI'} = 'http://�T�[�o�[/�p�X/data/';

#=> �Y�t�t�@�C���̓��[���ɓY�t�����ɃT�[�o�[��ɕۑ� (1:����^0:���Ȃ�)
#  * ���[���ɂ͕ۑ����URI���}������܂��B1M�𒴂���悤�ȃt�@�C�����󂯎��ꍇ�́A
#    ���[���Y�t�͔����A�T�[�o�[��ɕۑ�����悤�ɂ��܂��傤�B
$INI{'NoAttach'} = 0;

#=> �^�C�g�� (TITLE�v�f���ŕ\��)
$INI{'Title'} = '�t�H�[���[��';

# �� �t�H�[���y�[�W��URL (����URL�ȊO����͑��M�ł��Ȃ��B%7E��~�Ə���)
#$INI{'SetUrl'} = 'webpower.jp/';


#---<�f�U�C���ݒ�>-------------------------------------------------------------


#=> BODY�v�f�̑��� (<BODY ****>��****�̕���)
$INI{'body'} = 'text="#000000" bgcolor="#FFEEDD"';

# �� �O��CSS�t�@�C����[�A�h���X]
$INI{'css'} = '';

# �� �m�F�y�[�W�̃e�[�u���̍��ږ��̔w�i�F
$INI{'BG-COLOR1'} = '#99CCFF';

# �� �m�F�y�[�W�̃e�[�u���̍��ڂ̔w�i�F
$INI{'BG-COLOR2'} = '#FFFFCC';

#=> �m�F�y�[�W�㕔�ɕ\������HTML (_EOF_�s�͍폜���Ȃ�)
$INI{'header'} = <<'_EOF_';

<h1>���M���e�m�F</h1>

_EOF_

# �� CSS��` (STYLE�v�f�̓��e/_EOF_�s�͍폜���Ȃ�)


#---<����Ȑݒ�>---------------------------------------------------------------
#
#   ��ʓI�ȃT�[�o�[�ł͏�����Ԃ̂܂܂Ŗ�肠��܂���B
#   �K�v�ɉ����Đݒ肵�Ă��������B


#=> ���N�G�X�g���\�b�h (POST�^GET)
#  * ���M�� 'Method not implemented'���̃G���[���o��ꍇ��'GET'�ɂ��Ă��������B
#  * 'GET'�̏ꍇ�͕������������邽�߁A�������͓��͓r���Ő؂��ꍇ������܂��B
#  * J-SKY����A�N�Z�X�̏ꍇ�́A�����ł̐ݒ�Ɋ֌W�Ȃ������I��'GET'�ɂȂ�܂��B
$SYS{'rmethod'} = 'POST';

#=> ���̃X�N���v�g�̐ݒuURL (http://�Ŏw��)
#  * CGI-WRAP�����̗p���Ă���T�[�o�[(interQ��)�͐ݒ肵�Ă��������B
#$SENV{'SERVER_URI'} = 'http://www.domain.ne.jp/~foo/cgi-bin/formail.cgi';


#END_OF_INIT
#==============================================================================
# �� ���C�����[�`�� (�����ݒ肱���܂ŁB�ȉ��C���s�v�B�C�������ꍇ�͓����ۏ�)
#==============================================================================


# <�e��ݒ�E������>
#sub init
{

    binmode STDOUT;              #  Windows�nOS�̏ꍇ�͉��̍s�̃R�����g������
    $VERSION = q$FORMAIL/3.03$;  #  ���@�[�W�������(�ҏW�֎~)

    #  ���C�u�������[�h
    if (!-f $SYS{'jcodepl'}) {
        Show_ErrorPage('[001]���C�u���������o',
                       '���C�u������������܂���',
                       '<p>�@���̃V�X�e���𓮍삳����̂ɕK�v�ȃ��C�u����[jcode.pl]��������܂���B����̏ꏊ�ɑ��݂��Ă��邩�A�ꏊ�̎w��͐����������m�F���Ă��������B</p>');
    }
    if (!-f $SYS{'stdiopl'}) {
        Show_ErrorPage('[002]���C�u���������o',
                       '���C�u������������܂���',
                       '<p>�@���̃V�X�e���𓮍삳����̂ɕK�v�ȃ��C�u����[stdio.pl]��������܂���B����̏ꏊ�ɑ��݂��Ă��邩�A�ꏊ�̎w��͐����������m�F���Ă��������B</p>');
    }
    require $SYS{'stdiopl'};
    require $SYS{'jcodepl'};

    if ((split(/\//, $stdio::version))[1] < 9.04) {
        Show_ErrorPage('[002]���C�u�����o�[�W�����G���[',
                       '���C�u�����̃o�[�W�������Ⴂ�܂�',
                       '<p>�@���̃V�X�e���𓮍삳����̂ɕK�v�ȃ��C�u����[stdio.pl]�́Av9.04�ȍ~���g�p���Ă��������B</p>');
    }


    #  stdio.pl�����ݒ�
    $stdio::max_byte = $SYS{'maxsize'} * 1024;  # ��M�\�ő�e�� (�L���o�C�g)
    $stdio::sendmail = $SYS{'sendmail'};        # sendmail�̃p�X


    #  �\�[�X�R�[�h�̊����R�[�h�F��
    if (ord "��" == 0xb4 || ord "��"  == -76) {
        $JCODE = "euc";
        $CHARSET = '; charset=EUC-JP';
    } elsif (ord "��" == 0x8a || ord "��" == -118) {
        $JCODE = "sjis";
        $CHARSET = '; charset=Shift_JIS';
    } elsif (ord "��"  == 0x1b) {
        $JCODE = "jis";
        $CHARSET = '; charset=ISO-2022-JP';
    }

    #  ���ϐ� / �W�����̓f�[�^�ݒ�
    %SENV = %STDIO = ();
    @FORM_DATA = &stdio::getFormData(\%STDIO, 2, $JCODE, "\t", $SYS{'TempDir'});
    $SENV{'HTTP_REFERER'} = substr($ENV{'HTTP_REFERER'}, 0, 200);
    $SENV{'HTTP_REFERER'} =~ s/%7E/~/gi;
    $SENV{'HTTP_USER_AGENT'} = substr($ENV{'HTTP_USER_AGENT'}, 0, 200);
    $SENV{'HTTP_USER_AGENT'} =~ tr/<>"&/()'-/;
    if ($SENV{'SCRIPT_URI'}) {
        ($SENV{'SERVER_NAME'}, $SENV{'SCRIPT_PATH'}) = (split /\//, $SENV{'SCRIPT_URI'}, 4)[2,3];
        $SENV{'SCRIPT_PATH'} = "/$SENV{'SCRIPT_PATH'}";
    } else {
        $SENV{'SCRIPT_PATH'} = $ENV{'SCRIPT_NAME'};
        $SENV{'SERVER_NAME'} = $ENV{'SERVER_NAME'};
        $SENV{'SCRIPT_URI'}  = "http://$SENV{'SERVER_NAME'}$SENV{'SCRIPT_PATH'}";
    }
    $SENV{'SCRIPT_NAME'} = $1 if ($ENV{'SCRIPT_NAME'} =~ /([^\\\/]+$)/);
    $SENV{'REMOTE_ADDR'} = $ENV{'REMOTE_ADDR'};
    if ($SENV{'REMOTE_HOST'} eq $SENV{'REMOTE_ADDR'} || !$SENV{'REMOTE_HOST'}) {
        $SENV{'REMOTE_HOST'} = gethostbyaddr(pack('C4',split(/\./, $SENV{'REMOTE_ADDR'})),2);
        $SENV{'REMOTE_HOST'} = $SENV{'REMOTE_ADDR'} if (!$SENV{'REMOTE_HOST'});
    }

    #  PC/iMODE/J-SKY�̔���(UA���x�肪�\�Ȃ��߁AIP�ƃ����z�ł�����)
    if ($SENV{'HTTP_USER_AGENT'} =~ /^DoCoMo/ &&
       ($SENV{'REMOTE_HOST'} =~ /\.docomo\.ne\.jp$/ || $SENV{'REMOTE_ADDR'} =~ /^(210\.153\.84|210\.136\.161|203\.138\.45)/)) {
        $USER_AGENT = "iMODE";
    } elsif ($SENV{'HTTP_USER_AGENT'} =~ /^J-PHONE/ && 
       ($SENV{'REMOTE_HOST'} =~ /\.jp-[chknqrst]\.ne\.jp/ || $SENV{'REMOE_ADDR'} =~ /^(211\.8\.159|211\.8\.49|210\.134\.83|210\.146\.60|210\.169\.193|211\.127\.183)/)) {
        $USER_AGENT = "J-SKY";
    } else {
        $USER_AGENT = "OTHER";
    }
    #$SENV{'HTTP_USER_AGENT'}=$ENV{'HTTP_USER_AGENT'}="DoCoMo/1.0/P209is/c10";$USER_AGENT="iMODE"; #  for debug.

}
# </�e��ݒ�E������>



    # <�Z�L�����e�B�[�`�F�b�N>

        #  �ő�o�C�g���`�F�b�N
        if ($stdio::max_byte < $ENV{'CONTENT_LENGTH'}) {
            Show_ErrorPage('[003]�W�����̓f�[�^�T�C�Y����',
                           '�f�[�^���傫�����܂�',
                           "<p>�@���M���ꂽ�f�[�^�̃T�C�Y������̃T�C�Y�𒴉߂������߁A�����𒆒f���܂����B���M�f�[�^�̃T�C�Y�����������čĎ��s���Ă��������B</p>");
        }

        #  �t�H�[���f�[�^�̗L���`�F�b�N
        if (!@FORM_DATA) {
            Show_ErrorPage('[004]�W�����̓f�[�^�Ȃ�',
                           '�f�[�^������܂���',
                           "<p>�@���N�G�X�g���ꂽ�f�[�^�ɓ��e������܂���B���̃V�X�e���͒��ڋN�����邱�Ƃ͂ł��܂���B���K�̃t�H�[������đ��M���Ă��������B</p>");
        }

        #  ���\�b�h�`�F�b�N(POST���\�b�h���Ή��@�킪����J-PHONE�̓`�F�b�N�ΏۊO)
        if ($USER_AGENT ne "J-SKY" && $SYS{'rmethod'} eq "POST" && $ENV{'REQUEST_METHOD'} ne "POST") {
            Show_ErrorPage('�s���ȗv�����\�b�h',
                           '�v�����\�b�h���s���ł�',
                           "<p>�@�v��(���N�G�X�g)���\�b�h��&quot;POST&quot;�ȊO�ŌĂяo����܂����B���̃V�X�e���̓Z�L�����e�B�[�ی�̂��߁A&quot;POST&quot;���\�b�h�ȊO�ł̌Ăяo���͋����Ă���܂���B</p>");
        }

        #  �Q�ƌ��`�F�b�N(REFERER��f���Ȃ��g�ѓd�b�̓`�F�b�N�ΏۊO)
        if ($USER_AGENT eq "OTHER" && $INI{'SetUrl'} && ($SENV{'HTTP_REFERER'} !~ /$INI{'SetUrl'}/i || $SENV{'HTTP_REFERER'} !~ /$SENV{'SCRIPT_URI'}/)) {
            Show_ErrorPage('[005]�s���ȎQ�ƌ�',
                           '�Q�ƌ��̒l���s���ł�',
                           "<p>�@���ϐ�&quot;HTTP_REFERER&quot;(�Q�ƌ�)�̒l���s��(�����o�A�������͑��̃T�C�g��URL�����o)�ł��B���̃V�X�e���̓Z�L�����e�B�[�ی�̂��߁A����̃y�[�W�ȊO����̎Q��(���ڃA�N�Z�X)�͋����Ă���܂���B�������܂����A���K�̃t�H�[������đ��M���Ă��������B</p>"
                         . "<p>�@���ϐ������ς���A�v���P�[�V����(�l�p�̃v���N�V�T�[�o�[��t�@�C�A�E�H�[���\�t�g�����܂܂�܂�)���g�p����Ă���ꍇ�́A���̃G���[�̌����ƂȂ��Ă����\�\��������܂��̂ŁA�ꎞ�I�ɊO���čđ��M���Ă��������B���s�ւ����������Đ\���󂠂�܂���B</p>\n"#);
                         );
        }

    # </�Z�L�����e�B�[�`�F�b�N>


    # <�^�C���A�E�g�̃Z�b�V��������E�Y�t�ꎞ�t�@�C�����폜 />
    if (opendir DIR, $SYS{'TempDir'}) {
        my($dir_size) = 0;
        while ($_ = readdir DIR) {
            if ((/\.ses$/ || /\.tmp$/) && (-M "$SYS{'TempDir'}$_") * 86400 > 900) {
                unlink "$SYS{'TempDir'}$_";
            } else {
                $dir_size += (-s "$SYS{'TempDir'}$_");
            }
        }
        closedir DIR;

        #  �T�[�o�[���Ɉꎞ�ۑ�����f�[�^������̃T�C�Y�����`�F�b�N
        if ($max_buff && $max_buff < $dir_size) {
            Show_ErrorPage('[006]�o�b�t�@�T�C�Y�I�[�o�[',
                           '���Ԃ������čđ��M���Ă�������',
                           "<p>�@�������܃T�[�o�[���̊���o�b�t�@�T�C�Y�𒴉߂��Ă����Ԃ̂��߁A�������p���ł��܂���B�������܂����A���Ԃ������čĎ��s���Ă��������B���s�ւ����������Đ\���󂠂�܂���B</p>\n");
        }
    }

    # <�Z�b�V����ID/�t�H�[��ID�̎擾 => �Z�b�V��������ǂݏo�� />
    if ($STDIO{'_SESSION-ID'} =~ /^[0-9A-F]{16}-(\w+)$/) {
        my(%flag, $ses_file);

        $FORM_ID = $1;
        $SESSION_ID   = $STDIO{'_SESSION-ID'};
        $SESSION_FILE = "$SYS{'TempDir'}$SESSION_ID.ses";

        $ses_file = "$SYS{'TempDir'}$SENV{'SCRIPT_NAME'}.$FORM_ID.ses";

        #  ���M�����t���b�O�̊m�F (��x���M�h�~) => �w��URL�փW�����v or ���M�����y�[�W�\�� => �I��
        if (stdio::getSession($ses_file, \%flag, $SESSION_ID)) {
            if ($flag{'redirect'} ne "") {
                print "Location: $flag{'redirect'}\n"
                    . "\n";
            } else {
                &Show_SubmittedPage;
            }
            exit;
        }

        #  �Z�b�V�����t�@�C���J�� or �^�C���A�E�g
        if (!open IN, $SESSION_FILE) {
            Show_ErrorPage('[007]�Z�b�V�����A�E�g',
                           '���̃Z�b�V�����͖����ł�',
                           "<p>�@�L���ȃZ�b�V��������ǂݏo�����Ƃ��ł��܂���ł����B�����Ƃ��Ĉȉ��̂��Ƃ��l�����܂��B�������M�̍�Ɠr���ł������ꍇ�A����܂ł̑��M���e�͎����܂����B�������܂����A�ŏ������蒼���Ă��������B���s�ւ����������Đ\���󂠂�܂���B</p>\n"
                         . "<ul>\n"
                         . "  <li>�f�[�^�̑��M���Ȃ��܂܁A��莞�Ԃ��o�߂����B</li>\n"
                         . "  <li>���M��Ƀu���E�U��[�߂�]�Ŗ߂��čđ��M���悤�Ƃ����B</li>\n"
                         . "  <li>���M��Ƀ����[�h(�ēǍ�)���s�����B</li>\n"
                         . "</ul>\n");
        }
        @session = <IN>;
        close IN;

    # <�Z�b�V����ID������or�l���s�� => �Z�b�V����ID/�t�H�[��ID�̐ݒ� />
    } else {
        $FORM_ID = substr $STDIO{'_FORM-ID'}, 0, 20;
        $FORM_ID =~ tr/A-Za-z0-9_//cd;  #  �Z�L�����e�B�[�K�[�h
        $FORM_ID = 'DEFAULT' if ($FORM_ID eq "");
        $SESSION_ID   = sprintf("%02X%02X%02X%02X%X", (split /\./, $ENV{'REMOTE_ADDR'})[0..3], time) . "-$FORM_ID";
        $SESSION_FILE = $SYS{'TempDir'} . "$SESSION_ID.ses";
    }

    # <�y�[�WID�̐ݒ�>
    if ($STDIO{'_FORM-PAGE'} eq "") {
        $PAGE_ID = "<DEFAULT>";
    } else {
        $PAGE_ID = substr $STDIO{'_FORM-PAGE'}, 0, 40;
        $PAGE_ID =~ tr/A-Za-z0-9_.\-//cd;  #  �Z�L�����e�B�[�K�[�h
    }

#  �R�}���h�t�@�C�����̐ݒ�
$command_file = $STDIO{'_COMMAND-FILE'};
undef $command_file if ($command_file =~ /(^\/|\.\.\/\.\.\/\.\.|[^\w\-\.\/])/);  # �Z�L�����e�B�[�K�[�h


#  �R�}���h�t�@�C����ǂݍ���
if (open IN, "$command_file") {
    my($data, $data2, $flag, $flag2);
    read IN, $data, (-s $command_file);
    close IN;

    $data =~ s/<!--(.|\s)*-->//g;
    $data =~ s/\r\n|\r/\n/g;
    foreach (split /\n/, $data) {
        if ($flag) {
            if (/^<\//) {
                $STDIO{$key} = $data2;
                push @FORM_DATA, $key;
                $flag = $flag2 = 0;
                $key = $data2 = "";
            } else {
                if ($STDIO{$key} && !$flag2) {
					$STDIO{$key} .= "\t";
					$flag2 = 1;
				}
				$data2 .= "$_\n";
                $STDIO{$key} .= "$_\n";
            }
        } elsif (/^<([^>]+)>([^<]*)<\//) {
            my($key, $val) = ($1, $2);
            push @FORM_DATA, $key;
            if (!$STDIO{$key}) {
				$STDIO{$key} = $val;
			} else {
            	$STDIO{$key} .= "\t$val";
            }
        } elsif (/^<([^>]+)>/) {
            $key = $1;
            $flag = 1;
        }
    }
}

#  �R�}���h�ǂݍ���
&Read_Command;

# <�u���L�[�̐ݒ�>
%key_name = (
    'CODE'    => '���M�ԍ�',
    'TIME'    => '���M����',
    'HOST'    => '�����[�g�z�X�g',
    'ADDR'    => '�����[�g�A�h���X',
    'AGENT'   => '�G�[�W�F���g',
    'NAME'    => '���O',
    'MAIL'    => '���[���A�h���X',
    '_SUBJECT' => '����'
);

#  ������͖�/���菉���l
$type{'MAIL'} = $type{'_TO'} = $type{'_REPLY-TO'} = 'MAIL';
$type{'CC'} = $type{'_BCC'} = 'MAIL2';
$type{'NAME'} = $type{'_SUBJECT'} = $type{'_SUBJECT2'} = 'TEXT';
$maxval{'NAME'}     = 256 if ($maxval{'NAME'} > 256);
$maxval{'_SUBJECT'} = 256 if ($maxval{'_SUBJECT'} > 256);
$maxval{'_SUBJECT2'}= 256 if ($maxval{'_SUBJECT2'} > 256);
$NOBLANK{'MAIL'} = 1 if ($STDIO{'_CCOPY'});


#  �m�F�y�[�W����̑��M�ł͖���
if (!$STDIO{'__SUBMIT__'}) {

    #  �t�H�[���f�[�^�`�F�b�N
    ($err_msg, @list) = &Check_FormData;

    # <���͕s��������ꍇ>
    if ($err_msg) {
        my($form_page) = $STDIO{'_FORM-PAGE'};

        #  �P�[�^�C�̏ꍇ => B�v�f�r�� �S�p�J�i���p�ϊ�
        if ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
            $err_msg =~ s/<\/?b>//g;
            jcode::z2h_sjis(\$err_msg);
        }

        #  �Y�t�t�@�C���폜
        unlink @stdio::file if (@stdio::file);

        #  �G���[���b�Z�[�W��UL�v�f�ɂ��ӏ�����
        $err_msg = "<ul>\n"
                 . $err_msg
                 . "</ul>";

        # <�t�H�[���y�[�W��HTML��� �����͏�Ԃŕ\��>
        undef $form_page if ($form_page =~ /(^\/|\.\.\/\.\.\/\.\.|[^\w\-\.\/])/);  # �Z�L�����e�B�[�K�[�h
        if (open IN, $form_page) {
            my(@element, $data, $next_file, $hidden1, $hidden2, %i);
            my($i) = 0;

            read IN, $data, (-s $form_page);
            close IN;

            $next_file = (split /\t/, $STDIO{'_NEXT'}, 2)[0];
            $hidden1 = qq|<input type="hidden" name="_SESSION-ID" value="$SESSION_ID" />|;
            $hidden2 = qq|<input type="hidden" name="_FORM-PAGE" value="$STDIO{'_FORM-PAGE'}" />|;
            undef $next_file if ($next_file =~ /(^\/|\.\.\/\.\.\/\.\.|[^\w\-\.\/])/);  # �Z�L�����e�B�[�K�[�h

            $data =~ s/<!--\/COMMENT-->/-->/gi;
            $data =~ s/<!--COMMENT-->/<!--/gi;
            $data =~ s/<!--PRINT//gi;
            $data =~ s/PRINT-->//gi;
            $data =~ s/<!--ERROR MESSAGE-->/$err_msg/;
            $data =~ s/<!--#[^>]+>//g;  #  �Z�L�����e�B�[�K�[�h(SSI�R�}���h�폜)

            if (-f $SESSION_FILE) {
                $data =~ s/(<form\s+[^>]+>)/Check_FormAction($1,$hidden1)/egi;
            }
            if ($data !~ /name=["']?_FORM-PAGE["']?/i && $next_file) {
                $data =~ s/(<form\s+[^>]+>)/Check_FormAction($1,$hidden2)/egi;
            }

            #  �t�H�[�����M����`�F�b�N
            sub Check_FormAction #($form_tag, $hidden)
            {
                my($form_tag, $hidden) = @_;
                #return $_[0] =~ /$SENV{'SCRIPT_NAME'}/ ? "$data$_[1]" : $_[0];
                return $form_tag =~ /$SENV{'SCRIPT_NAME'}/ ? "$form_tag$hidden" : $form_tag;
            }

            @element = split(/(<[^>]*>)/, $data);
            undef $data;

            foreach (@element) {
                my($name, $value);

                if (/^<input|select|option|textarea/i) {

                    #  ���̓^�C�v�擾
                    if (/^<\/select/i) {
                        $select_name = "";
                    } elsif (/^<\//) {
                        $data .= $_;
                        $i ++;
                        next;
                    } elsif (/^<select/i) {
                        $multiple = / multiple/i ? 1 : 0;
                        $type = "select";
                    } elsif (/^<option/i) {
                        $type = "option";
                    } elsif (/^<textarea/i) {
                        $type = "textarea";
                    } elsif (/ type=['"]?(\w+)['"]?/i) {
                        $type = $1 ne "" ? $1 : "text";
                    }
                    $type =~ tr/A-Z/a-z/;

                    #  image file hidden submit reset button�̏ꍇ�͖���
                    if ($type eq "hidden" || $type eq "submit" || $type eq "reset" ||
                        $type eq "button" || $type eq "file" || $type eq "image") {
                        $data .= $_;
                        $i ++;
                        next;
                    }

                    #  checked/selected����������
                    s/ checked(=['"]?checked['"]?)?//g;
                    s/ selected(=['"]?selected['"]?)?//g;
                    s/ *\/>/>/g;  #  for XHTML

                    #  ���͖��擾
                    if ($type eq "option") {
                        $name = $select_name;
                    } else {
                        $name = $1 if (/ name=([^ >]*)/i);
                        $name =~ s/^["']//g;
                        $name =~ s/["']$//g;
                        $i{$name} = !defined $i{$name} ? 0 : $i{$name} + 1;
                        if ($type eq "select") {
                            $select_name = $name;
                            $data .= $_;
                            $i ++;
                            next;
                        }
                    }

                    #  �l���擾
                    $value = $1 if (/ value=([^ >]*)/i);
                    $value =~ s/^["']//g;
                    $value =~ s/["']$//g;
                    if ($type eq "textarea" || ($type eq "option" && $value eq "")) {
                        $value = $element[$i+1];
                    }

                    #  �����͒l�������l�ɐݒ�
                    if ($type eq "text" || $type eq "password") {
                        my($value2) = (split /\t/, $STDIO{$name})[$i{$name}];
                        s/ value=[^ >]*//i;
                        s/>/ value="$value2">/i;
                    } elsif ($type eq "textarea") {
                        my($value2) = (split /\t/, $STDIO{$name})[$i{$name}];
                        $value2 =~ s/<br \/>/\n/g;
                        if ($element[$i+1] =~ /^(<\/textarea>)$/i) {
                            $element[$i+1] = "$value2$1";
                        } else {
                            $element[$i+1] = $value2;
                        }
                    } else {
                        my($value2) = (split /\t/, $STDIO{$name})[$i{$name}];
                        my($name2);
                        foreach (split /\t/, $STDIO{$name}) {
                            if ($_ eq $value) {
                                $name2 = $_;
                                last;
                            }
                        }
                        $name2 = $STDIO{$name} if (!defined $name2);
                        if ($type eq "checkbox" || $type eq "radio") {
                            if (($name2 eq $value && $value ne "") || ($type eq "checkbox" && $value eq "" && $name2 =~ /^ON$/i)) {
                                s/>/ checked="checked">/;
                            }

                        } elsif ($type eq "option") {
                            if ($multiple && $name2 eq $value) {
                                s/^<option/<option selected="selected"/i;
                            } elsif ($value eq $value2) {
                                s/^<option/<option selected="selected"/i;
                            }
                        }
                    }
                }
                $data .= $_;
                $i ++;
            }

            #  HTML�o�͊J�n
            print "Content-Type: text/html\n";
            print "Content-Length: " . length($data) . "\n";
            print "\n";

            print $data;
            exit;
        }
        # </�t�H�[���y�[�W��HTML��� �����͏�Ԃŕ\��>

        $title = $DATA{'_TITLE'} eq "" ? $INI{'Title'} : $DATA{'_TITLE'};
        $body  = $DATA{'_BODY'}  eq "" ? $INI{'Body'}  : $DATA{'_BODY'};
        $link_css = $DATA{'_CSS'} eq "" ? $INI{'css'}  : $DATA{'_CSS'};
        $link_css = qq[<link rel="stylesheet" type="text/css" href="$link_css" />\n] if ($link_css);

        #  �G���[���b�Z�[�W������\��
        print "Content-Type: text/html", $CHARSET, "\n";
        print "\n";
        print <<_EOF_;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
$link_css<title>$title [���͕s��]</title>
</head>
<body $body>

<h1>���͕s��</h1>
<p>�@�t�H�[���̓��͓��e�ɕs��������܂��B������x�m�F�̂����đ��M���Ă��������B</p>
$err_msg

</body>
</html>
_EOF_

        exit;

    }
    # </���͕s��������ꍇ>


    #  �Y�t�t�@�C�����̏d�����M�΍�J�n
    Check_DuplicationSubmit("begin") if ($USER_AGENT !~ /^(iMODE|J-SKY)$/);

    #  �y�[�WID��t�^ => �d���f�[�^�͏㏑��
    my($i) = 0;
    unshift @list, $PAGE_ID;
    foreach (@session) {
        if ((split /\t/, $_, 2)[0] eq $PAGE_ID) {
            last;
        }
        $i ++;
    }
    $session[$i] = join("\t", @list) . "\n";

}


#  ���̃y�[�W������ꍇ or ���M�O�m�F�̏ꍇ
if (!$STDIO{'_SUBMIT'}) {

    #  �Z�b�V������ۑ�
    if (!open OUT, ">$SESSION_FILE") {
        Show_ErrorPage('[008]�t�@�C�������G���[',
                       '�Z�b�V�����t�@�C���̏������݂��ł��܂���',
                       "<p>�@�Z�b�V�����t�@�C���̏������݂��ł��܂���B�Z�b�V�����t�@�C���ւ̏������ݗp�A�N�Z�X�����^�����Ă��Ȃ���\�\��������܂��B</p>");
    }
    print OUT @session;
    close OUT;

    #  �Z�b�V�������128KB���� or 20���߂ňُ�ƌ��Ȃ������I�� => �Z�b�V������� => �G���[���b�Z�[�W
    if ((-s $SESSION_FILE) > 131072 || $#session > 20) {
        unlink $SESSION_FILE;
        Show_ErrorPage('[009]�p�����[�^�[�G���[');
    }

    #  �m�F�y�[�W�\��
    if ($STDIO{'_NEXT'} =~ /^confirm$/i || $STDIO{'_NEXT'} eq "") {
        &Show_ConfirmPage(*session);

    #  ���y�[�W�փW�����v
    } elsif ($STDIO{'_NEXT'} =~ /^http/) {
        print "Location: $STDIO{'_NEXT'}?$SESSION_ID\n"
            . "\n";

    #  ���y�[�W��\��
    } else {
        my($data, $next_file, $hidden);

        $next_file = $STDIO{'_NEXT'};
        undef $next_file if ($next_file =~ /(^\/|\.\.\/\.\.\/\.\.|[^\w\-\.\/])/);  # �Z�L�����e�B�[�K�[�h
        $hidden    = qq|<input type="hidden" name="_SESSION-ID" value="$SESSION_ID" />|
                   . qq|<input type="hidden" name="_FORM-PAGE" value="$next_file" />|;

        if (!open IN, $next_file) {
            Show_ErrorPage('[010]�t�@�C���Ǎ��G���[',
                           '�t�@�C���̓ǂݍ��݂��ł��܂���',
                           "<p>�@�t�H�[���t�@�C���̓ǂݍ��݂��ł��܂���B�t�H�[���t�@�C��������̏ꏊ�ɑ��݂��Ȃ��A�t�H�[���t�@�C���̓ǂݍ��ݗp�A�N�Z�X�����^�����Ă��Ȃ���\�\��������܂��B</p>");
        }
        read IN, $data, (-s $next_file);
        close IN;
        $data =~ s/(<form\s+([^>]+)>)/$1$hidden/i;

        #  HTML�\���J�n
        print "Content-Type: text/html\n";
        print "Content-Length: " . length($data) . "\n";
        print "\n";

        print $data;

    }

    exit;
}


    if (!@session) {
        Show_ErrorPage('[007]�Z�b�V�����A�E�g',
                       '���̃Z�b�V�����͖����ł�',
                       "<p>�@�L���ȃZ�b�V��������ǂݏo�����Ƃ��ł��܂���ł����B�����Ƃ��Ĉȉ��̂��Ƃ��l�����܂��B�������M�̍�Ɠr���ł������ꍇ�A����܂ł̑��M���e�͎����܂����B�������܂����A�ŏ������蒼���Ă��������B���s�ւ����������Đ\���󂠂�܂���B</p>\n"
                     . "<ul>\n"
                     . "  <li>�f�[�^�̑��M���Ȃ��܂܁A��莞�Ԃ��o�߂����B</li>\n"
                     . "  <li>���M��Ƀu���E�U��[�߂�]�Ŗ߂��čđ��M���悤�Ƃ����B</li>\n"
                     . "  <li>���M��Ƀ����[�h(�ēǍ�)���s�����B</li>\n"
                     . "</ul>\n");
    }

    #  ���M�����t���b�O�̊m�F (��x���M�h�~)
    if (!$STDIO{'_SESSION-ID'}) {
        my(%flag, $id, $ses_file);

        $ses_file = "$SYS{'TempDir'}$SENV{'SCRIPT_NAME'}.$FORM_ID.ses";
        if ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
            $id = "$FORM_ID.$SENV{'HTTP_USER_AGENT'}";
        } else {
            $id = "$FORM_ID.$SENV{'REMOTE_ADDR'}";
        }

        #  ���M�����t���b�O�̊m�F (��x���M�h�~) => �w��URL�փW�����v or ���M�����y�[�W�\�� => �I��
        if (stdio::getSession($ses_file, \%flag, $SESSION_ID)) {
            if ($flag{'redirect'} ne "") {
                print "Location: $flag{'redirect'}\n"
                    . "\n";
            } else {
                &Show_SubmittedPage;
            }

            exit;
        }
    }

    &Submit_Email(*session);




#------------------------------------------------------------------------------
# �� �t�H�[���f�[�^���`�F�b�N���� (Check_FormData)
#
#     �ďo�� : 
#     ��  �� : �Z�b�V����ID
#     �߂�l : �G���[���b�Z�[�W, ���X�g
#------------------------------------------------------------------------------

sub Check_FormData #(void)
{

    #  ! �Ǐ��ϐ��錾
    my(
        $err_msg,   # �G���[���b�Z�[�W
        @list,
        %flag,
        $i
    );


    foreach (@FORM_DATA) {
        my($key, $val) = ($_, $STDIO{$_});
        my($key_name)  = $key_name{$key} eq "" ? $key : $key_name{$key};

        #  2��ڈȍ~�͓����L�[�̓p�X
        next if ($flag{$key});
        $flag{$key} = 1;

        $val =~ s/^\t//;

        #  �ő啶�����̐ݒ�
        $maxval{$key} = 2048 if ($type{$key} ne 'INT' && $type{$key} ne 'YEN' && !$maxval{$key} && !$STDIO{"$key->name"});

        #  �S�p�p�����̔��p�ϊ�
        if ($z2hset{$key}) {
            my($from) = q[�O�P�Q�R�S�T�U�V�W�X�`�a�b�c�d�e�f�g�h�i�j�k�l�m�n�o�p�q�r�s�t�u�v�w�x�y�����������������������������������������������������{�|�^���Q�b���I�H�h�f�������������F�G�O�C�i�j�o�p�����@];
            my($to)   = q[0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-/=_|*!?"'#$\%&@:;^,(){}<> ];
            jcode::tr(\$val, $from, $to);
        }

        # <�^�`�F�b�N>

            #  �t�@�C���^�T�C�Y�`�F�b�N
            if ($STDIO{"$key->name"}) {
                if (!$SYS{'UseMultipart'}) {
                    unlink $key;
                    $err_msg .= qq|  <li>�t�@�C���̓Y�t�͂ł��܂���B</li>\n|;

                } else {
                    my($file_name) = $STDIO{"$key->name"};

                    #  �t�@�C�������s�� or 64�o�C�g��
                    if (($file_name =~ /[^\w\-\[\]\(\).]/ && $INI{'NoAttach'}) || length $STDIO{"$key->name"} > 64) {
                        my($suffix) = $1 if ($file_name =~ /(\.[A-Za-z0-9]+)$/);
                        $file_name  = $$ + time;
                        $file_name .= $suffix;
                    }

                    $i ++;
                    $file_name = "$i-$file_name";

                    #  �t�@�C���T�C�Y�`�F�b�N
                    if ($maxval{$key} && $STDIO{"$_->size"} > $maxval{$key}) {
                        $err_msg .= qq|  <li>�A�b�v���[�h�\\��1������̃t�@�C���T�C�Y��| . stdio::setComma($maxval{$key}) . qq|�o�C�g�܂łł��B</li>\n|;
                        unlink $key;  #  �Y�t�t�@�C���폜
                    } elsif ($minval{$key} && $STDIO{"$_->size"} < $minval{$key}) {
                        $err_msg .= qq|  <li>�A�b�v���[�h�\\��1������̃t�@�C���T�C�Y��| . stdio::setComma($maxval{$key}) . qq|�o�C�g�ȏ�ł��B</li>\n|;
                        unlink $key;  #  �Y�t�t�@�C���폜
                    } elsif (!$STDIO{"$_->size"}) {
                        $err_msg .= qq|  <li>�t�@�C���̒��g������܂���B��t�@�C���̃A�b�v���[�h�͂ł��܂���B</li>\n|;
                        unlink $key;  #  �Y�t�t�@�C���폜

                    #  �l�� (>\t�T�[�o�[���̃t�@�C���p�X\t�t�@�C����\t���[�U�[���ł̃t�@�C���p�X\t�t�@�C���T�C�Y\tMIME�^�C�v)
                    } else {
                        $val = qq(>\t$STDIO{$key}\t$file_name\t$STDIO{"$key->path"}\t$STDIO{"$key->size"}\t$STDIO{"$key->type"});
                    }
                }

            #  ���[���A�h���X�^�`�F�b�N
            } elsif ($type{$key} eq "MAIL") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val && $val !~ /^[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6}$/) {
                        $err_msg .= qq|  <li><b>$key_name</b>�̓��[���A�h���X�`���ɂȂ��Ă��܂���B(���p�Ő��������͂��Ă�������)</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if ($_ && ! /^[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6}$/) {
                            $err_msg .= qq|  <li><b>$key_name</b>�̓��[���A�h���X�`���ɂȂ��Ă��܂���B(���p�Ő��������͂��Ă�������)</li>\n|;
                            last;
                        }
                    }
                }

            #  ������L���[���A�h���X�^�`�F�b�N
            } elsif ($type{$key} eq "MAIL2") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val && $val !~ /^[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6}(,[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6})*$/) {
                        $err_msg .= qq|  <li><b>$key_name</b>�̓��[���A�h���X�`���ɂȂ��Ă��܂���B(���p�Ő��������͂��Ă�������)</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if ($_ && ! /^[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6}(,[-+.\w]{1,30}@[-+.\w]*[-A-Za-z0-9]{2,30}\.[A-Za-z]{2,6})*$/) {
                            $err_msg .= qq|  <li><b>$key_name</b>�̓��[���A�h���X�`���ɂȂ��Ă��܂���B(���p�Ő��������͂��Ă�������)</li>\n|;
                            last;
                        }
                    }
                }

            #  URL�^�`�F�b�N
            } elsif ($type{$key} eq "URL") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    $val = "" if ($val eq 'http://');
                    if ($val && $val !~ /^https?:\/\/[\w|\:\@\-]+\.[\w|\:\!\#\%\=\&\-\|\@\~\+\.\?\/]+$/) {
                        $err_msg .= qq|  <li><b>$key_name</b>��URL�`���ɂȂ��Ă��܂���B(���p�Ő��������͂��Ă�������)</li>\n|;
                    }
                } else {
                    my(@url);
                    foreach (split /\t/, $val) {
                        $_ = "" if ($_ eq 'http://');
                        if ($_ && ! /^https?:\/\/[\w|\:\@\-]+\.[\w|\:\!\#\%\=\&\-\|\@\~\+\.\?\/]+$/) {
                            $err_msg .= qq|  <li><b>$key_name</b>��URL�`���ɂȂ��Ă��܂���B(���p�Ő��������͂��Ă�������)</li>\n|;
                            last;
                        }
                        push @url, $_;
                    }
                    $val = join "\t", @url if (@url);
                }

            #  �ʉ݌^�`�F�b�N
            } elsif ($type{$key} eq "YEN") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val =~ /\D/) {
                        $err_msg .= qq|  <li><b>$key_name</b>�͔��p�����œ��͂��Ă��������B</li>\n|;
                    } elsif ($val ne "") {
                        1 while $val =~ s/(.*\d)(\d\d\d)/$1,$2/;
                        $val .= "�~";
                    }
                } else {
                    my(@yen);
                    foreach (split /\t/, $val) {
                        if (/\D/) {
                            $err_msg .= qq|  <li><b>$key_name</b>�͔��p�����œ��͂��Ă��������B</li>\n|;
                            last;
                        } elsif ($_ ne "") {
                            1 while s/(.*\d)(\d\d\d)/$1,$2/;
                            $_ .= "�~";
                            push @yen, $_;
                        }
                    }
                    $val = join "\t", @yen if (@yen);
                }

            #  �����^�`�F�b�N
            } elsif ($type{$key} eq "FIGURE") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val =~ /\D/) {
                        $err_msg .= qq|  <li><b>$key_name</b>�͔��p�����œ��͂��Ă��������B</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if (/\D/) {
                            $err_msg .= qq|  <li><b>$key_name</b>�͔��p�����œ��͂��Ă��������B</li>\n|;
                            last;
                        }
                    }
                }

            #  �����^�`�F�b�N
            } elsif ($type{$key} eq "INT") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val !~ /^-?\d+$/) {
                        $err_msg .= qq|  <li><b>$key_name</b>�͔��p�����œ��͂��Ă��������B</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if (! /^-?\d+$/) {
                            $err_msg .= qq|  <li><b>$key_name</b>�͔��p�����œ��͂��Ă��������B</li>\n|;
                            last;
                        }
                    }
                }

            #  ���p�����^�`�F�b�N
            } elsif ($type{$key} eq "BYTE") {
                $val =~ s/<br \/>//gi;
                if ($val !~ /\t/) {
                    if ($val =~ /[^\x20-\x7e]/) {
                        $err_msg .= qq|  <li><b>$key_name</b>�͔��p�œ��͂��Ă��������B</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if (/[^\x20-\x7e]/) {
                            $err_msg .= qq|  <li><b>$key_name</b>�͔��p�œ��͂��Ă��������B</li>\n|;
                            last;
                        }
                    }
                }

            #  �_���^�`�F�b�N
            } elsif ($type{$key} eq "BOOLEAN") {
                $val =~ s/<br \/>//gi;
                $val =~ s/\t//g;
                $val = !$val || $val =~ /off|no|false/i ? '������' : '�͂�';

            #  �m�[�}���e�L�X�g�^�`�F�b�N
            } elsif ($type{$key} eq "TEXT") {
                $val =~ s/<br \/>//gi;
            }

        # </�^�`�F�b�N>


        #  �K�{���ڂ̖����̓`�F�b�N
        if ($NOBLANK{$key} && ($val eq "" || $val =~ /\t\t/ || $val =~ /\t$/)) {
            $err_msg .= qq|  <li><b>$key_name</b>�͕K�{���ڂ̂��ߋL�����Ă��������B</li>\n|;

        #  ��x���͈�v�̊m�F
        } elsif ($chkset{$key} && !($val eq "" || $val =~ /\t\t/ || $val =~ /\t$/)) {
            my($flag);
            my($default) = (split /\t/, $val)[0];
            foreach (split /\t/, $val) {
                if ($default ne $_) {
                    $err_msg .= qq|  <li><b>$key_name</b>���m�F�̂��߂ɍē��͂��ꂽ���̂ƈ�v���܂���B</li>\n|;
                    $flag = 1;
                    last;
                }
            }
            if (!$flag) {
                $val = $default;
            }

        #  �ő�l/��������������/�ő�`�F�b�N�\���`�F�b�N
        } elsif ($maxval{$key}) {
            if ($type{$key} eq "INT" || $type{$key} eq "YEN") {
                if ($val !~ /\t/) {
                    if ($val > $maxval{$key}) {
                        $err_msg .= qq|  <li><b>$key_name</b>��$maxval{$key}�ȉ��̒l���L�����Ă��������B</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if ($_ > $maxval{$key}) {
                            $err_msg .= qq|  <li><b>$key_name</b>��$maxval{$key}�ȉ��̒l���L�����Ă��������B</li>\n|;
                            last;
                        }
                    }
                }
            } elsif ($type{$key} eq "DEFINE") {
                my($count) = $val =~ tr/\t/\t/;
                if ($maxval{$key} && $count >= $maxval{$key}) {
                    $err_msg .= qq|  <li><b>$key_name</b>�őI���ł���̂�$maxval{$key}�܂łł��B</li>\n|;
                }
            } else {
                if ($val !~ /\t/) {
                    my($length) = length $val;
                    if ($length > $maxval{$key}) {
                        $err_msg .= qq|  <li><b>$key_name</b>��$maxval{$key}�o�C�g�ȓ�(�S�p�ł��̔���)�ŋL�����Ă��������B(���� $length�o�C�g)</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        my($length) = length;
                        if ($length > $maxval{$key}) {
                            $err_msg .= qq|  <li><b>$key_name</b>��$maxval{$key}�o�C�g�ȓ�(�S�p�ł��̔���)�ŋL�����Ă��������B(���� $length�o�C�g)</li>\n|;
                            last;
                        }
                    }
                }
            }

        #  �ŏ��l/�w�蕶�����s��/�Œ�`�F�b�N�\���`�F�b�N
        } elsif ($minval{$key}) {
            if ($type{$key} eq "INT" || $type{$key} eq "YEN") {
                if ($val !~ /\t/) {
                    if ($val < $minval{$key}) {
                        $err_msg .= qq|  <li><b>$key_name</b>��$minval{$key}�ȏ�̒l���L�����Ă��������B</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        if ($_ < $minval{$key}) {
                            $err_msg .= qq|  <li><b>$key_name</b>��$minval{$key}�ȏ�̒l���L�����Ă��������B</li>\n|;
                            last;
                        }
                    }
                }
            } elsif ($type{$key} eq "DEFINE") {
                my($count) = $val =~ tr/\t/\t/;
                if ($minval{$key} && $count <= $minval{$key}) {
                    $err_msg .= qq|  <li><b>$key_name</b>�őI���ł���̂�$minval{$key}�܂łł��B</li>\n|;
                }
            } else {
                if ($val !~ /\t/) {
                    my($length) = length $val;
                    if ($length < $minval{$key}) {
                        $err_msg .= qq|  <li><b>$key_name</b>��$minval{$key}�o�C�g�ȏ�(�S�p�ł��̔���)���L�����Ă��������B(���� $length�o�C�g)</li>\n|;
                    }
                } else {
                    foreach (split /\t/, $val) {
                        my($length) = length;

                        if ($length < $minval{$key}) {
                            $err_msg .= qq|  <li><b>$key_name</b>��$minval{$key}�o�C�g�ȏ�(�S�p�ł��̔���)���L�����Ă��������B(���� $length�o�C�g)</li>\n|;
                            last;
                        }
                    }
                }
            }
        }

        #  �G���[���������
        if (!$err_msg) {
            #$val = $val_name{$val} if ($valset{$key});

            #  �������ڂ̌���
            $val =~ s/\t/$joinset{$key}/g if (defined $joinset{$key});

            #  �Z�b�V�������Ɋ܂߂Ȃ��L�[�Ŗ��� => �Z�b�V��������ۑ�
            if ($key !~ /^_(SET:[A-Z0-9]+|NOBLANK|SESSION-ID|NEXT|FORM-ID|FORM-PAGE|MAX-[A-Z]+|MIN-[A-Z]+|JOIN\(.*\)|Z2HCONV|EQCHECK)$/) {
                $key =~ s/\t/&#9;/g;
                $val =~ s/\t/&#9;/g;
                push @list, "$key=>$val";
            }
        }
    }

    #  �K�{���ڂ̖����̓`�F�b�N(checkbox/select�v�f���̃L�[������Ȃ����ڗp)
    foreach(keys %NOBLANK) {
        if ($_ && !$flag{$_} && $STDIO{$_} eq "") {
            my($key_name)  = $key_name{$_} eq "" ? $_ : $key_name{$_};
            $err_msg .= qq|  <li><b>$key_name</b>�͕K�{���ڂ̂��ߑI�����Ă��������B</li>\n|;
        }
    }

    return $err_msg, @list;
}#


#------------------------------------------------------------------------------
# �� ���M�O�m�F�y�[�W�\�� (Show_ConfirmPage)
#
#     �ďo�� : Show_MainPage, Show_ChatPage, Login_Chat, Show_LoginPage
#     ��  �� : (�Z�b�V����ID, )
#     �߂�l : (�I��)
#------------------------------------------------------------------------------

sub Show_ConfirmPage #(*data)
{

    #  ��������
    local(*data) = @_;

    #  ! �Ǐ��ϐ��錾
    my(
        @form_data,
        $title,
        $body,
        $confirm,
        %DATA,
        %hidden
    );


    #  �z�񂩂�n�b�V��
    @form_data = Array_to_Hash(\@data, \%DATA);

    #  �m�F�y�[�W�ŕ\�����Ȃ�����
    foreach (split /\t/, $DATA{'_HIDDEN'}) { $hidden{$_} = 1; }
    $hidden{'CODE'} = $hidden{'TIME'} = 1;

    #  �m�F�y�[�W��HTML�\���J�n
    foreach (@form_data) {
        my($key, $val) = ($_, $DATA{$_});
        my($key_name)  = $key_name{$key} eq "" ? $key : $key_name{$key};

        #  �B�����ڂłȂ�?
        if (!$hidden{$_}) {
            if ($val =~ /^>\t/) {
                my($name, $path, $size) = (split /\t/, $val)[2..4];
                $val = "$path (" . stdio::setComma($size) . "�o�C�g)";
            }
            $val =~ s/  /�@/g;
            $val = '<span class="blank">(������)</span>' if ($val eq "");

            #  �P�[�^�C����
            if ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
                $val =~ tr/\t/\n/;
                if ($key eq '_SPLIT') {
                    $confirm .= $val eq "" ? "\n\n" : "�� $val\n\n";
                } elsif ($key !~ /^_/) {
                    $confirm .= "[$key_name]\n"
                              . "$val\n\n";
                }

            #  �p�\�R������
            } else {
                $val =~ s/\t/<br \/>/g;
                if ($key eq '_SPLIT') {
                    $val = '�@' if ($val eq "");
                    $confirm .= qq|  </table>\n|
                             .  qq|    <h2>$val</h2>\n|
                             .  qq|  <table border="0" cellpadding="5" width="80%" id="AutoNumber1" cellspacing="1">\n|;

                } elsif ($key =~ /^(NAME|MAIL|_SUBJECT)$/ || $key !~ /^_/) {
                    $confirm .= qq|    <tr>\n|
                             .  qq|      <th nowrap="nowrap" bgcolor="$INI{'BG-COLOR1'}" width="30%"><div class="bg_blue">$key_name</div></th>\n|
                             .  qq|      <td bgcolor="$INI{'BG-COLOR2'}" width="70%"><kbd>$val</kbd></td>\n|
                             .  qq|    </tr>\n|;
                }
            }
        }
    }

    $header= $DATA{'_PAGE-HEADER'} eq "" ? $INI{'header'} : $DATA{'_PAGE-HEADER'};
    $footer= $DATA{'_PAGE-FOOTER'} eq "" ? $INI{'footer'} : $DATA{'_PAGE-FOOTER'};
    $title = $DATA{'_TITLE'} eq "" ? $INI{'Title'} : $DATA{'_TITLE'};
    $body  = $DATA{'_BODY'}  eq "" ? $INI{'Body'}  : $DATA{'_BODY'};
    $link_css = $DATA{'_CSS'} eq "" ? $INI{'css'}  : $DATA{'_CSS'};
    $link_css = qq[<link rel="stylesheet" type="text/css" href="$link_css" />\n] if ($link_css);

    #  HTML�\���J�n for �P�[�^�C
    if ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
        my($data);
        my($method) = ($SYS{'rmethod'} eq "GET" || $USER_AGENT eq "J-SKY") ? "GET" : "POST";

        jcode::z2h_sjis(\$confirm);
        $data = <<_EOF_;

<html lang="ja">
<head>
<title>$title [���M���e�m�F]</title>
</head>
<body $body>
<h1>�����M���e�m�F</h1>
<pre>
$confirm
</pre>
<form action="$SENV{'SCRIPT_NAME'}" method="$method">
  <input type="hidden" name="_SESSION-ID" value="$SESSION_ID" />
  <div align="center">
    <input type="submit" name="_SUBMIT" value="���M" />
  </div>
</form>
</body>
</html>
_EOF_

        print "Content-Type: text/html\n";
        print "Content-Length: " , length($data), "\n";
        print "\n";
        print $data;
        #  --


    #  HTML�\���J�n for PC
    } else {
        print "Content-Type: text/html", $CHARSET, "\n";
        print "\n";
        print <<_EOF_;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=shift_jis" />
<title>�t���[���C�^�[�Ŗ��O���ւ̂��₢���킹</title>
<meta name="Keywords" content="�Z��,�t���[���C�^�[,�Ŗ��O��" />
<meta name="Description" content="�Z��E���m�I�уR���T���^���g���t���[���C�^�[�Ŗ��O���ւ̂��₢���킹" />
<meta name="robots" content="index,follow" />
<link href="https://secure1846.sakura.ne.jp/zenta1.com/css/contact_import.css" rel="stylesheet" type="text/css" />
</head>
<body>
<a name="top" id="top"></a>
<div id="structure">

<h1><img src="../img/contact/logo.jpg" alt="�t���[���C�^�[�Ŗ��O��" /></h1>
<h2>�Z��t���[���C�^�[�Ŗ��O���y��v�R���e���c�z</h2>

<!--�O���[�o���i�r�Q�[�V���� -->

<ul id="navi">
<li id="contact"><span class="pop"><a href="https://secure1846.sakura.ne.jp/zenta1.com/contact/contact.html" class="popup"><img src="../img/contact/navi/contact.jpg"/><img src="../img/contact/navi/contact_voice.jpg" class="large"/></a></span></li>
<li id="case"><span class="pop"><a href="http://www.zenta1.com/img/works/sample.pdf" target="_blank" class="popup"><img src="../img/contact/navi/case.jpg"/><img src="../img/contact/navi/case_voice.jpg" class="large"/></a></span></li>
<li id="works"><span class="pop"><a href="http://www.zenta1.com/works.html" class="popup"><img src="../img/contact/navi/works.jpg"/><img src="../img/contact/navi/works_voice.jpg" class="large"/></a></span></li>
<li id="profile"><span class="pop"><a href="http://www.zenta1.com/profile.html" class="popup"><img src="../img/contact/navi/profile.jpg" /><img src="../img/contact/navi/profile_voice.jpg" class="large"/></a></span></li>
</ul>



<!--�R���e���c�͂�������@container�J�n -->
<div id="contents">

<!-- ���� -->
<div id="left_side">

<a href="http://aqua-d.biz/zenta/index.html"><img src="../img/common/bt_toppage.gif" alt="�u�t���[���C�^�[�Ŗ��O���v�̃g�b�v�y�[�W�֖߂�" width="200" height="22" /></a>

<!-- �u���O -->
<div id="blog_link02">
<div id="blog_link">
<p>
<a href="http://menchi-da.blog.so-net.ne.jp/" target="_blank">���ԃA�N�Z�X<br />
<strong>�V�O�O�O�O</strong>�I�[�o�[�I<br />
<strong>�u�t���[���C�^�[�O���̂������n�E�X���[�J�[��r�v</strong> </a><br />
�X�̍H���X������n�E�X���[�J�[�܂�20�Јȏ��
��������r�B���̈ꕔ�n�I�����J���܂��I</p>
</div>
</div>

<!-- ���[�N�V�[�g -->
<div id="worksheet_link">
<p>
<a href="https://secure1846.sakura.ne.jp/zenta1.com/worksheet/worksheet.html"><span class="or">�����ŃQ�b�g�I</span><br />
<strong>���Ȃ��́w�S�̒ꂩ��[���ł���Ɓx���ȒP�ɂ킩��
�V���̃��[�N�V�[�g</strong></a>�͂����炩�火<br />
<a href="https://secure1846.sakura.ne.jp/zenta1.com/worksheet/worksheet.html"><img src="../img/common/get_free.jpg" alt="�����ŃQ�b�g" /></a></p>
</div>
</div>
<!-- ���������܂� -->


<!--�E���L�� -->
<div id="kiji">

<div id="contact">
<h2>�t���[���C�^�[�Ŗ��O���ւ̂��₢���킹</h2>

<p id="step">���q�l�����́c�c<strong>���e�m�F���</strong>�c�c���₢���킹����</p>

<table border="0" cellpadding="7" width="80%" cellspacing="1">
$confirm
</table>

<form action="$SENV{'SCRIPT_NAME'}" method="$SYS{'rmethod'}">
  <input type="hidden" name="_SESSION-ID" value="$SESSION_ID" />
  <hr size="1" />
  <div align="center" class="button">
    <input type="submit" name="_SUBMIT" value="�@�@���@�M�@�@" /><input type="button" value="�@�@���@���@�@" onClick="history.back()" /><br />
    <font size="1">�������x���ꍇ������܂����A���M�{�^���͈�x���������Ă��΂炭���҂��������B</font>
  </div>
  <hr size="1" />
</form>
$footer

</div>
<div id="toppage"><a href="#top">�� PAGE TOP</a></div>
</div>

</div>
<!--�E���L���I�� -->

<!--�@�R�s�[���C�g -->
<div id="copyrignt">Copyright&copy;2009 Zenta Shiina. All Rights Reserved. </div>

</div>
<!--�@structure�I�� -->

</body>
</html>

_EOF_
    }

    exit;
}#


#------------------------------------------------------------------------------
# �� �{���M��̏��� (Submit_Email)
#
#     �ďo�� : main
#     ��  �� : (*�f�[�^�z��)
#     �߂�l : (�I��)
#------------------------------------------------------------------------------

sub Submit_Email #(*data)
{

    #  ��������
    local(*data) = @_;

    #  ! �Ǐ��ϐ��錾
    my(
        %DATA,
        $space,         # �L�[�ƒl�̋�؂�
        $from,          # �Ǘ��҈����[���̍��o�l
        $title,         # ���M�����y�[�W�̃^�C�g��(TITLE�v�f���e)
        $body,          # ���M�����y�[�W��BODY�v�f�̑���
        $link_css,      # ���M�����y�[�W��CSS�t�@�C���ւ�LINK�v�f
        $mailbody1,     # ���[���{��(�Ǘ��҂ɑ��M��������)
        $mailbody2,     # ���[���{��(���M�҂ɑ��M��������)
        $time,          # �Y�t�t�@�C�����ɕt����UTC���Ԃ̃V���A���l
        @form_data,
        %hidden         # ���M�҈����[���ŏȗ�����L�[��
    );


    #  �z�񂩂�n�b�V��
    @form_data = Array_to_Hash(\@data, \%DATA);

    #  �L�[�ƒl�̋�؂� (���s or ��)
    $space = $DATA{'_TYPE'} ? "\n" : " ";

    $title = $DATA{'_TITLE'} eq "" ? $INI{'Title'} : $DATA{'_TITLE'};
    $body  = $DATA{'_BODY'}  eq "" ? $INI{'Body'}  : $DATA{'_BODY'};
    $link_css = $DATA{'_CSS'} eq "" ? $INI{'css'}  : $DATA{'_CSS'};
    $link_css = qq[<link rel="stylesheet" type="text/css" href="$link_css">\n] if ($link_css);

    $time = time . "-";
    $DATA{'CODE'} = time . int(rand(10));
    $DATA{'TIME'} = scalar gmtime(time + $INI{'TimeZone'} * 3600);
    $DATA{'HOST'} = $SENV{'REMOTE_HOST'};
    $DATA{'ADDR'} = $SENV{'REMOTE_ADDR'};
    $DATA{'AGENT'}= $SENV{'HTTP_USER_AGENT'};

    #  CC���[���{���ɖ��L���Ȃ�����
    foreach (split /\t/, $DATA{'_HIDDEN2'}) { $hidden{$_} = 1; }

    # <���[���{���쐬�J�n>
    foreach (@form_data) {
        my($key, $val) = ($_, $DATA{$_});
        my($key_name)  = $key_name{$key} eq "" ? $key : $key_name{$key};

        #  �Y�t�t�@�C���̏ꍇ(">"�Ŏn�܂�) ���� : (>\t�T�[�o�[���̃t�@�C���p�X\t�t�@�C����\t���[�U�[���ł̃t�@�C���p�X\t�t�@�C���T�C�Y\tMIME�^�C�v)
        if ($val =~ /^>\t/) {
            my($fname, $name, $path, $size) = (split /\t/, $val)[1..4];
            $name = "$DATA{'_CODE'}$name";

            #  ���`�ς݃t�@�C�����ɕύX => �p�X�� @attach_file1 �Ɋi�[
            if (rename $fname, "$SYS{'TempDir'}$name") {
                push @attach_files1, "$SYS{'TempDir'}$name";
            }

            #  ���[�����M���Ȃ�(�T�[�o�[���ɕۑ�����)�ꍇ
            if ($INI{'NoAttach'} && $SYS{'DataDirURI'}) {
                $val = "$path (" . stdio::setComma($size) . "�o�C�g)\n"
                     . qq[$SYS{'DataDirURI'}$time$name\n];

            } else {
                $val = "$path (" . stdio::setComma($size) . "�o�C�g)";
            }

        #  �ʏ�e�L�X�g���̏ꍇ
        } else {
            $val =~ s/\t/$space/g;
        }
        $val = '(������)' if ($key ne '_SPLIT' && $val eq "");

        #  �f�[�^���烁�[���{�����쐬
        if ($key eq '_SPLIT') {
            $mailbody1 .= $val eq "" ? "\n\n" : "�� $val\n\n";
            $mailbody2 .= $val eq "" ? "\n\n" : "�� $val\n\n" if (!$hidden{$_} && $DATA{'_CCOPY'});
        } elsif ($key !~ /^_/) {
            $mailbody1 .= "[$key_name]$space"
                        . "$val\n\n";
            $mailbody2 .= "[$key_name]$space"
                        . "$val\n\n" if (!$hidden{$_} && $DATA{'_CCOPY'});
        }
    }
    # </���[���{���쐬�J�n>


    # <�Ǘ��҈����[�����M>
    {

        $DATA{'_HEADER'} .= "\n" if ($DATA{'_HEADER'});
        $mailbody1 =<<_EOF_;
$DATA{'_HEADER'}
$mailbody1
$DATA{'_FOOTER'}

�� ���M���̏�� -----------------------------------------------------

 ���M����     : @{[scalar(gmtime(time + 3600 * $INI{'TimeZone'}))]}
 ���M�ԍ�     : $DATA{'CODE'}

 �T�[�o�[��   : $SENV{'SERVER_NAME'} : $ENV{'SERVER_PORT'}
 �X�N���v�g�� : $SENV{'SCRIPT_PATH'}
 �v�����\\�b�h : $ENV{'REQUEST_METHOD'}
 �Q�ƌ�       : $SENV{'HTTP_REFERER'}
 �G�[�W�F���g : $SENV{'HTTP_USER_AGENT'}
 �z�X�g��(IP) : $SENV{'REMOTE_HOST'} ($SENV{'REMOTE_ADDR'})

---------------------------------------------------------------------
_EOF_

        #  HTML�p�̎��̎Q�Ƃ����Ԃɒu��
        $mailbody1 =~ s/<br \/>/\n/g;
        $mailbody1 =~ s/&lt;/</g;
        $mailbody1 =~ s/&gt;/>/g;
        $mailbody1 =~ s/&quot;/"/g;
        $mailbody1 =~ s/&amp;/&/g;


        #  �w�b�_�̐ݒ�
        $DATA{'_SUBJECT'} = '(����)' if ($DATA{'_SUBJECT'} eq "");
        $DATA{'_SUBJECT2'} = $DATA{'_SUBJECT'} if ($DATA{'_SUBJECT2'} eq "");
        $DATA{'MAIL'} = 'anonymous@on.the.net' if ($DATA{'MAIL'} eq "");
        if ($DATA{'NAME'} !~ /^[\s�@]*$/) {
            $from = "$DATA{'NAME'} <$DATA{'MAIL'}>";
        } else {
            $from = $DATA{'MAIL'};
        }
        $INI{'mailto'} = $DATA{'_TO'} if (!$INI{'mailto'});

        #  �Ǘ��҈����[���w�b�_�[
        %header1 = (
            "To"         => $INI{'mailto'},
            "From"       => $from,
            "Subject"    => $DATA{'_SUBJECT'},
            "X-Mailer"   => $VERSION,
            "X-MailID"   => $DATA{'CODE'}
        );
        $header1{'X-Priority'} = $DATA{'_PRIORITY'} if ($DATA{'_PRIORITY'} =~ /^[1-5]$/);
        $header1{'Bcc'} = $DATA{'_BCC'};
        $header1{'Cc'}  = $DATA{'_CC'};


        {
            my(@attach_files, $encode);

            $encode = $DATA{'_ENCODE'};
            foreach (@attach_files1) {
                my($file_name, $new_file, $mime_type);

                $mime_type = Get_MimeType($_);
                $file_name = $1 if (/([^\\\/]+)$/);
                $new_file  = "$SYS{'DataDir'}$time$file_name";
                $file_name =~ s/^\d+-//;
                if ($INI{'NoAttach'}) {
                    rename $_, $new_file;
                } else {
                    push @attach_files, "$_;$mime_type;$file_name";
                }
            }

            #  ���ۂɃ��[�����M
            if (!stdio::sendmail(\%header1, $mailbody1, 0, $encode, @attach_files)) {
                Show_ErrorPage('[012]���[�����M�G���[',
                               '���[���̑��M���ł��܂���',
                               "<p>�@���[���̑��M���ł��܂���B���[�����M�v���O����[sendmail]�ւ̃p�X���������ݒ肳��Ă��Ȃ��A���s�A�N�Z�X�����^�����Ă��Ȃ���\�\��������܂��B</p>");

           }
        }
    }
    # </�Ǘ��҈����[�����M>


    # <���M�҈����[�����M>
    if ($DATA{'_CCOPY'}) {
        my(@attach_files2, $encode);

        $encode = $DATA{'_ENCODE2'} ? $DATA{'_ENCODE2'} : $DATA{'_ENCODE'};

        #  �e���v���[�g�t�@�C������ǂݍ���
        if ($DATA{'_TEMPLATE'}) {
            $mailbody2 = $DATA{'_TEMPLATE'};
            $mailbody2 =~ s/{\$([^}]+)}/$DATA{$1}/g;

        #  �ʏ�̃��[���{��
        } else {
            $DATA{'_HEADER2'} .= "\n" if ($DATA{'_HEADER2'});
            $mailbody2 = <<_EOF_;
$DATA{'NAME'} �l

$DATA{'_HEADER2'}
$mailbody2
$DATA{'_FOOTER2'}
_EOF_

        }

        $mailbody2 =~ s/<br \/>/\n/g;
        $mailbody2 =~ s/&lt;/</g;
        $mailbody2 =~ s/&gt;/>/g;
        $mailbody2 =~ s/&quot;/"/g;
        $mailbody2 =~ s/&amp;/&/g;


        #  ���M�҈����[���w�b�_�[
        my(%header2) = (
            "To"         => $from,
            "From"       => $DATA{'_FROM'},
            "Subject"    => $DATA{'_SUBJECT2'},
            "X-Mailer"   => $VERSION,
            "X-MailID"   => $DATA{'CODE'}
        );
        $header2{'X-Priority'} = $DATA{'_PRIORITY2'} if ($DATA{'_PRIORITY2'} =~ /^[1-5]$/);
        $header2{'Reply-To'} = $DATA{'_REPLY'} if ($DATA{'_REPLY'});


        #  ���M�҈��Y�t�t�@�C��
        foreach (split /\t/, $DATA{'_ATTACHMENT-FILE'}) {
            my($mime_type) = Get_MimeType($_);

            next if (/(^\/|\.\.\/|[^\w\-\.\/])/);  # �Z�L�����e�B�[�K�[�h
            push @attach_files2, "$SYS{'FileDir'}$_;$mime_type" if (-f "$SYS{'FileDir'}$_");
        }

        #  ���ۂɃ��[�����M
        if (!stdio::sendmail(\%header2, $mailbody2, 0, $encode, @attach_files2)) {
            Show_ErrorPage('[015]���[�����M�G���[',
                           '���[���̑��M���ł��܂���',
                           "<p>�@���[���̑��M���ł��܂���B���[�����M�v���O����[sendmail]�ւ̃p�X���������ݒ肳��Ă��Ȃ��A���s�A�N�Z�X�����^�����Ă��Ȃ���\�\��������܂��B</p>");
        }
    }
    # </���M�҈����[�����M>


    #  �Z�b�V�������
    unlink $SESSION_FILE;

    #  �Y�t�t�@�C�����̏d�����M�΍�I��
    Check_DuplicationSubmit("free") if ($USER_AGENT !~ /^(iMODE|J-SKY)$/);

    #  �Y�t�t�@�C���폜
    unlink @attach_files1 if (@attach_files1);

    #  ���M�����t���b�O�̊m�� (��x���M�h�~)
    {
        my($id, %flag, $ses_file);

        $ses_file = "$SYS{'TempDir'}$SENV{'SCRIPT_NAME'}.$FORM_ID.ses";
        if ($STDIO{'_SESSION-ID'}) {
            $id = $SESSION_ID;
        } elsif ($USER_AGENT =~ /^(iMODE|J-SKY)$/) {
            $id = "$FORM_ID.$SENV{'HTTP_USER_AGENT'}";
        } else {
            $id = "$FORM_ID.$SENV{'REMOTE_ADDR'}";
        }
        $flag{'submited'} = 1;
        $flag{'redirect'} = $DATA{'_REDIRECT'} if ($DATA{'_REDIRECT'} ne "");
        stdio::setSession($ses_file, \%flag, $id, 600);
    }

    #  �w��URL�փW�����v or ���M�����y�[�W�\�� => �I��
    if ($DATA{'_REDIRECT'}) {
        print "Location: $DATA{'_REDIRECT'}\n"
            . "\n";

    } else {
        &Show_SubmittedPage;
    }

    exit;
}#


#------------------------------------------------------------------------------
# �� �d�����M�΍� (Check_DuplicationSubmit)
#
#     �ďo�� : (�ėp)
#     ��  �� : (�t�@�C����)
#     �߂�l : (�Ȃ�)
#------------------------------------------------------------------------------

sub Check_DuplicationSubmit
{

    #  ��������
    my($action) = @_;

    #  ! �Ǐ��ϐ��錾
    my($id, $ses_file, %ses);

    $ses_file = "$SYS{'TempDir'}$SENV{'SCRIPT_NAME'}.check.ses";
    $id = $FORM_ID . $ENV{'REMOTE_ADDR'};

    if ($action eq "free") {
        stdio::setSession($ses_file, "", $id);
        return;
    }

    if (stdio::getSession($ses_file, \%ses, $id)) {
        if ($ses{'<SESSION-ID>'} && $ses{'<SESSION-ID>'} ne $SESSION_ID) {
            unlink "$SYS{'TempDir'}$ses{'<SESSION-ID>'}.ses";
            foreach (split /\t/, $ses{'<PAGE-ID>'}) {
                if (-f $ses{$_}) {
                    unlink $ses{$_};
                } else {
                    foreach (split /\t/, $ses{$_}) {
                        unlink $_;
                    }
                }
            }
            undef %ses;
        } elsif ($ses{$PAGE_ID} ne "") {
            if (-f $ses{$PAGE_ID}) {
                unlink $ses{$PAGE_ID};
            } else {
                foreach (split /\t/, $ses{$PAGE_ID}) {
                    unlink $_;
                }
            }
        }
    }
    $ses{'<SESSION-ID>'} = $SESSION_ID;
    $ses{'<PAGE-ID>'} .= "$PAGE_ID\t";
    $ses{$PAGE_ID} = join "\t", @afile if (@afile);
    stdio::setSession($ses_file, \%ses, $id);

    return;
}


#------------------------------------------------------------------------------
# �� �Z�b�V�����ێ��p�̔z����n�b�V���ɂ��� (Array_to_Hash)
#
#     �ďo�� : Show_ConfirmPage Submit_Email
#     ��  �� : (*�f�[�^�z��, *�f�[�^�n�b�V��)
#     �߂�l : (�L�[�̃��X�g)
#------------------------------------------------------------------------------

sub Array_to_Hash #(*array, *hash)
{

    #  ��������
    local(*array, *hash) = @_;

    #  ! �Ǐ��ϐ��錾
    my(@key_list);

    foreach (@array) {
        chomp;
        my(@list) = split /\t/;
        shift @list;
        foreach (@list) {
            s/&#9;/\t/g;
            my($key, $val) = split /=>/, $_, 2;
            $hash{$key} = $val;
            push @key_list, $key;
        }
    }

    return @key_list;
}


#------------------------------------------------------------------------------
# �� �g���q����MimeType���擾���� (Get_MimeType)
#
#     �ďo�� : (�ėp)
#     ��  �� : (�t�@�C����)
#     �߂�l : (MimeType) �Ή�������̂�������� 'application/octet-stream'
#------------------------------------------------------------------------------

sub Get_MimeType #($file)
{

    #  ��������
    my($file) = @_;

    #  ! �Ǐ��ϐ��錾
    my(%mime_type) = (
        'shtml' => 'text/html', 
        'stm'   => 'text/html',
        'hdml'  => 'text/hdml',
        'html'  => 'text/html',
        'htm'   => 'text/html',
        'xml'   => 'text/xml',
        'csv'   => 'text/plain',
        'txt'   => 'text/plain',
        'rtx'   => 'text/richtext',
        'css'   => 'text/css',
        'gif'   => 'image/gif',
        'jpeg'  => 'image/jpeg',
        'jpg'   => 'image/jpeg',
        'png'   => 'image/png',
        'bmp'   => 'image/bmp',
        'tiff'  => 'image/tiff',
        'tif'   => 'image/tiff',
        'ico'   => 'image/x-icon',
        'midi'  => 'audio/midi',
        'mid'   => 'addio/midi',
        'mp2'   => 'audio/mpeg',
        'mp3'   => 'audio/mpeg',
        'wav'   => 'audio/x-wav',
        'au'    => 'audio/basic',
        'zip'   => 'application/zip',
        'lzh'   => 'application/x-lzh',
        'lha'   => 'application/x-lzh',
        'swf'   => 'application/x-shockwave-flash',
        'js'    => 'application/x-javascript',
        'tar'   => 'application/x-tar',
        'gz'    => 'application/x-gzip',
        'pdf'   => 'application/pdf',
        'avi'   => 'video/x-msvideo',
        'mpeg'  => 'video/mpeg',
        'mpg'   => 'video/mpeg',
        'qt'    => 'video/quicktime',
        'mov'   => 'video/quicktime'
    );
    $file = $file =~ /\.(.+)$/ ? $1 : "";

    return defined $mime_type{$file} ? $mime_type{$file} : 'application/octet-stream';
}


#------------------------------------------------------------------------------
# �� �G���[�y�[�W�\�� (Show_ErrorPage)
#
#     �ďo�� : (�ėp)
#     ��  �� : (�G���[�^�C�v,�G���[�^�C�g��,���b�Z�[�W)
#     �߂�l : (�I��)
#------------------------------------------------------------------------------

sub Show_ErrorPage #($err_type, $err_title, $err_msg)
{

    #  ��������
    my($err_type, $err_title, $err_msg) = @_;

    $err_msg = $err_msg =~ /^<p>/i ? $err_msg : "<p>$err_msg</p>";

    #  ���X�|���X�w�b�_�o�� => HTML�\���J�n
    print "Content-Type: text/html", $CHARSET, "\n"
        . "Cache-Control: no-cache\n"
        . "Pragma: no-cache\n"
        . "\n";
    print <<_EOF_;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
<base href="$SENV{'SCRIPT_URI'}" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<title>$INI{'Title'} [�V�X�e���G���[]</title>
</head>
<body $INI{'Body'} class="ErrorPage">


<div class="error">
  <h2 class="error">&nbsp;<img border="0" src="$SENV{'SCRIPT_URI'}?[error]" alt="�G���[" width="28" height="28" /> <font color="#FF0000">$err_title</font></h2>
  $err_msg
  <br />
  <br />
  <br />
  <div align="center" class="bar">
    <small><a href="javascript:history.back()">[���߂�]</a> <a href="javascript:location.reload(true)">[�Ď��s]</a></small>
  </div>
  <p><small>�� �G���[���������Ȃ��ꍇ�͈ȉ��̏���Y���Ă��̃T�C�g�̊Ǘ��҂ւ��Ɖ�������B</small></p>
  <pre class="error-info" style="color:gray; font-size:12px">
  $err_type ($VERSION)
  TIME  :@{[scalar gmtime(time+$INI{'TimeZone'}*3600)]} (GMT$INI{'TimeZone'})
  IPADDR:$SENV{'REMOTE_HOST'} ($ENV{'REMOTE_ADDR'})
  AGENT :$ENV{'HTTP_USER_AGENT'}
  REFFER:$ENV{'HTTP_REFERER'}</pre>
</div>

</body>
</html>
_EOF_

    exit;
}#


#------------------------------------------------------------------------------
# �� CGI�o�R�Ńt�@�C���o�� (Show_File_by_CGI)
#
#     �ďo�� : (�ėp)
#     ��  �� : ���ʖ�
#     �߂�l : (�I��)
#------------------------------------------------------------------------------

sub Show_File_by_CGI #($name)
{

    #  ��������
    my($name) = @_;

    #  ! �Ǐ��ϐ��錾
    my($data, $flag, $type);

    while (<DATA>) {
        next if (/^#/);
        if (!$flag) {
            my($name2);
            chomp;
            ($name2, $type) = split /,/;
            next if ($name eq "");
            $flag = $name eq $name2 ? 2 : 1;
        } elsif (/^__SEPARATOR__/) {
            last if ($flag == 2);
            $flag = 0;
        } elsif ($flag == 2) {
            $data .= $_;
        }
    }

    if ($data ne "") {
        $type = 'application/octet-stream' if ($type eq "");
        binmode STDOUT;
        if ($type =~ /^(image|audio|video)\//) {
            my(@data);
            $data =~ tr/A-Fa-f0-9\r\n\t //cd;
            @data = split /\s+/, $data;
            print "Content-Type: ", $type, "\n";
            print "Content-Length: ", scalar @data, "\n";
            print "\n";
            foreach (@data) {
                print pack('C*', hex $_);
            }
        } else {
            print "Content-Type: ", $type, "\n";
            print "Content-Length: ", length $data, "\n";
            print "\n";
            print $data;
        }
    } else {
        print "Content-Type: text/html\n"
            . "Status: 204 No Content\n"
            . "\n";
    }

    exit;
}#


#==============================================================================
# �� ���M�����y�[�W�\�� (Show_SubmittedPage)
#==============================================================================

sub Show_SubmittedPage
{

    #  ���M�����y�[�W�\��
    print "Content-Type: text/html", $CHARSET, "\n";
    print "\n";
    print <<_EOF_;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
$link_css<title>$title [���M����]</title>
</head>
<body $body>
<h1>���M����</h1>

<p>�@�t�H�[���̃f�[�^�͐���ɑ��M����܂����B</p>

</body>
</html>
_EOF_

    return;
}#



#==============================================================================
# �� �R�}���h��ǂݍ��� (Read_Command)
#==============================================================================

sub Read_Command
{

    #  ! �Ǐ��ϐ��錾
    my(%i);

    #  ���͕K�{
    foreach (split /\t/, $STDIO{'_NOBLANK'}) {
        $NOBLANK{$_} = 1;
    }

    #  ��x���͊m�F����
    foreach (split /\t/, $STDIO{'_EQCHECK'}) {
        $chkset{$_}  = 1;
    }

    #  �S�p�p�����p�ϊ�
    foreach (split /\t/, $STDIO{'_Z2HCONV'}) {
        $z2hset{$_}  = 1;
    }

    # <�^��`>

        #  ���[���A�h���X�^
        foreach (split /\t/, $STDIO{'_SET:MAIL'}) {
            $type{$_} = "MAIL";
            $maxval{$_}  = 128;
        }

        #  ������L���[���A�h���X�^
        foreach (split /\t/, $STDIO{'_SET:MAIL2'}) {
            $type{$_} = "MAIL2";
            $maxval{$_}  = 256;
        }

        #  ��s�e�L�X�g�^
        foreach (split /\t/, $STDIO{'_SET:TEXT'}) {
            $type{$_} = "TEXT";
            $maxval{$_}  = 256;
        }

        #  URL(http)�^
        foreach (split /\t/, $STDIO{'_SET:URL'}) {
            $type{$_} = "URL";
            $maxval{$_} = 128;
        }

        #  �����^(������Ƃ��Ă�)
        foreach (split /\t/, $STDIO{'_SET:DIGIT'}) {
            $type{$_} = "FIGURE";
            $maxval{$_} = 256;
        }

        #  ���p(1�o�C�g)�^
        foreach (split /\t/, $STDIO{'_SET:BYTE'})  {
            $type{$_} = "BYTE";
            $maxval{$_} = 256;
        }

        #  �ʉ݌^(���l�^)
        foreach (split /\t/, $STDIO{'_SET:YEN'}) {
            $type{$_} = "YEN";
            $maxval{$_} = 999999999999999;
            $minval{$_} = 0;
        }

        #  �����^(���l�^)
        foreach (split /\t/, $STDIO{'_SET:INT'})  {
            $type{$_} = "INT";
            $maxval{$_} = 999999999999999;
            $minval{$_} = -999999999999999;
        }

        #  �_���^(YES/NO�^)
        foreach (split /\t/, $STDIO{'_SET:BOOLEAN'})  {
            $type{$_} = "BOOLEAN";
        }

        #  �Œ�l�^
        foreach (split /\t/, $STDIO{'_SET:DEFINE'}) {
            $type{$_} = "DEFINE";
        }

    # </�^��`>

    #  ---
    foreach (@FORM_DATA) {
        $i{$_} = 0 if (!defined $i{$_});
        my($data) = $STDIO{$_} =~ /\t/ ? (split /\t/, $STDIO{$_})[$i{$_}++] : $STDIO{$_};

        #  �ő�l(�o�C�g/�l/�`�F�b�N�\��)
        if (/^_MAX-VALUE\((\d{1,16})\)/) {
            my($max) = $1;
            if ($type{$_} eq "INT" || $type{$_} eq "YEN") {
                $maxval{$data} = $max if ($max >= -999999999999999 && $max <= 999999999999999);
            } elsif ($STDIO{"$_->name"}) {
                $maxval{$data} = $max;
            } else {
                $maxval{$data} = $max if ($max > 0 && $max <= 10240);
            }

        #  �ŏ��l(�o�C�g/�l/�`�F�b�N�\��)
        } elsif (/^_MIN-VALUE\((\d{1,16})\)/) {
            my($min) = $1;
            if ($type{$_} eq "INT" || $type{$_} eq "YEN") {
                $minval{$data} = $min if ($min >= -999999999999999 && $min <= 999999999999999);
            } elsif ($STDIO{"$_->NAME"}) {
                $minval{$data} = $min;
            } else {
                $minval{$data} = $min if ($min > 0 && $min <= 10240);
            }

        #  ��������
        } elsif (/^_JOIN\(([^\)]+)\)/) {
            $joinset{$1} = $data;

        #  �Y�t�t�@�C��
        } elsif ($STDIO{"$_->name"}) {
            push @afile, $STDIO{$_};
        }
    }

    return;
}

#  for Debug.

sub h #(void)
{

    print "Content-Type: text/html", $CHARSET, "\n"
        . "\n"
        . "<plaintext>\n";

}#

sub d #(@_)
{

    print "Content-Type: text/html", $CHARSET, "\n"
        . "\n"
        . "<plaintext>\n";
    print @_;

    exit;
}#


#******************************************************************************
# �� Show_File_by_CGI�֐��ŏo�͂���f�[�^
#
#   * "#"�Ŏn�܂�s�̓R�����g�ƌ��Ȃ������̑ΏۂƂ��Ȃ��B
#   * �N�G���[�����񂩈�����[���ʖ�]���w�� (filename.cgi?[���ʖ�])
#   * ���� : (1�s��=���ʖ�,MIME-TYPE �Z�p���[�^�s=__SEPARATOR__)
#******************************************************************************

__DATA__
error,image/gif
47 49 46 38 39 61 1c 00 1c 00 a1 00 00 00 00 00 ff 00 00 ff
ff ff bf bf bf 21 f9 04 01 00 00 03 00 2c 00 00 00 00 1c 00
1c 00 00 02 68 9c 8f a9 cb 18 1f 9a 4c 30 ce 59 df 95 d9 6e
d5 69 1f 15 8e 4e 28 9a 68 fa 65 82 90 a9 d5 1b b7 f3 0b 57
36 24 00 40 0e d9 b8 7a 3f 20 8b 31 f4 d1 74 9c 1b 11 57 43
3a 95 cb a0 94 87 a3 56 8f 87 e1 4b 6b f4 9c b0 b8 32 94 39
7e 98 c1 61 12 39 5b 2c 47 07 5e b3 3d ba ca 97 e8 fa be c6
0f 18 08 c8 27 88 32 50 00 00 3b
__SEPARATOR__
