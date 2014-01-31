
server_address='http://75.39.13.254/'
podcasts_folder_address= server_address + 'podcasts/'
#podcasts_folder_address = 'http://ec2-54-226-137-31.compute-1.amazonaws.com/podcasts/'

site_abs_directory='/vagrant/website/'
#site_abs_directory = '/var/www/'


if __name__ == '__main__':
    from sys import argv
    if argv[1] == 'podcasts_folder_address':
        print podcasts_folder_address

    elif argv[1] == 'site_abs_directory':
        print site_abs_directory
    
