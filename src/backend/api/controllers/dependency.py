from src.backend.domain.ports.inside.OneTurnElectionPort import OneTurnElectionPort
from src.backend.domain.ports.inside.ProportionalNationalElectionPort import ProportionalNationalElectionPort
from src.backend.domain.ports.outside.ResultsElectionsPort import ResultsElectionsPort
from src.backend.domain.services.GlobalElection.BuildCongress import BuildCongress
from src.backend.domain.services.GlobalElection.CongressPersonsElectedForEachDepartment import CongressPersonsElectedForEachDepartment
from src.backend.domain.services.GlobalElection.DeterminePercentageVoteByParty import DeterminePercentageVoteByParty
from src.backend.domain.services.GlobalElection.DetermineVoteByParty import DetermineVoteByParty
from src.backend.domain.services.GlobalElection.RegroupCongressPersonsByParties import RegroupCongressPersonsByParties
from src.backend.domain.services.GlobalElection.RepresentativeCongress import RepresentativeCongress
from src.backend.domain.services.GlobalElection.SelectCongressPerson import SelectCongressPersons
from src.backend.domain.services.GlobalElection.StabilityCongress import StabilityCongress
from src.backend.domain.services.OneTurnElection.ConstructDepartmentalAssemblies import ConstructDepartmentalAssemblies
from src.backend.domain.services.OneTurnElection.DeterminateAllElectedPersons import DeterminateAllElectedPersons
from src.backend.domain.services.OneTurnElection.DeterminateElectedPersonByDistrict import DeterminateElectedPersonByDistrict
from src.backend.domain.services.OneTurnElection.DeterminatePartyInfo import DeterminatePartyInfo
from src.backend.domain.services.OneTurnElection.OneTurnElectionService import OneTurnElectionService
from src.backend.domain.services.ProportionalDepartmentElection.CongressPersonByDepartment import CongressPersonByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.DeterminateSeatByPartyInDept import DeterminateSeatsByPartyInDept
from src.backend.domain.services.ProportionalDepartmentElection.DistrictsVoteFromDpt import DistrictsVoteFromDpt
from src.backend.domain.services.ProportionalDepartmentElection.ManageCongressPersonsByDepartment import ManageCongressPersonsByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.ModeDesignCongressPerson import ModeDesignCongressPerson
from src.backend.domain.services.ProportionalDepartmentElection.NumberCongressPerson import NumberCongressPerson
from src.backend.domain.services.ProportionalDepartmentElection.ProportionalDepartmentElectionService import ProportionalDepartmentElectionService
from src.backend.domain.services.ProportionalNationalElection.DeterminateSeatsByParty import DeterminateSeatsByParty
from src.backend.domain.services.ProportionalNationalElection.ProportionalNationalElectionService import ProportionalNationalElectionService
from src.backend.domain.services.ProportionalNationalElection.RemoveSmallParties import RemoveSmallParties
from src.backend.infrastructure.files.JsonFiles import JsonFiles
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection

def get_one_turn_election_service() -> OneTurnElectionPort:
    json_service = __get_json_service()
    stability_congress = StabilityCongress(577)
    representative_congress = RepresentativeCongress(577)
    build_congress = BuildCongress(stability_congress, representative_congress)
    elected_persons_by_district = DeterminateElectedPersonByDistrict()
    all_elected_persons = DeterminateAllElectedPersons(elected_persons_by_district)
    determinate_party_info = DeterminatePartyInfo()
    contruct_departmental_assemblies = ConstructDepartmentalAssemblies()
    election = OneTurnElectionService(json_service, all_elected_persons, build_congress, determinate_party_info, contruct_departmental_assemblies)
    return election

def get_proportional_national_election_service() -> ProportionalNationalElectionPort:
    json_service = __get_json_service()
    determine_vote_by_party = DetermineVoteByParty()
    determine_percentage_vote_by_party = DeterminePercentageVoteByParty()
    remove_small_parties = RemoveSmallParties()
    #TODO externalize conf
    determine_seats_by_parties = DeterminateSeatsByParty(577)
    select_congress_persons = SelectCongressPersons()
    regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
    representative_congress = RepresentativeCongress(577)
    stability_congress = StabilityCongress(577)
    build_congress = BuildCongress(stability_congress, representative_congress)
    election = ProportionalNationalElectionService(json_service, determine_vote_by_party, determine_percentage_vote_by_party, remove_small_parties, 
                                                    determine_seats_by_parties, select_congress_persons, regroup_congress_persons_by_parties, build_congress)
    return election

def get_proportional_departmental_election_service () -> ProportionalDepartmentElectionService:
    json_service = __get_json_service()
    total_congress_person = NumberCongressPerson()
    mode_design_congress_person = ModeDesignCongressPerson()
    districts_vote_from_dpt = DistrictsVoteFromDpt()
    determinate_vote_by_party = DetermineVoteByParty()        
    percentage_vote_by_party = DeterminePercentageVoteByParty()        
    determinate_seats_by_party_in_dept = DeterminateSeatsByPartyInDept()
    select_congress_persons = SelectCongressPersons()
    regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
    congress_persons_elected_for_each_department = CongressPersonsElectedForEachDepartment()

    congress_persons_by_departments = CongressPersonByDepartment(total_congress_person, mode_design_congress_person, districts_vote_from_dpt, 
                                                                determinate_vote_by_party, percentage_vote_by_party, determinate_seats_by_party_in_dept,
                                                                select_congress_persons, regroup_congress_persons_by_parties, congress_persons_elected_for_each_department)
    manage_congress_persons_by_department = ManageCongressPersonsByDepartment()        
    stability_congress = StabilityCongress(577)
    representative_congress = RepresentativeCongress(577)
    build_congress = BuildCongress(stability_congress, representative_congress)
    proportional_department_election_service = ProportionalDepartmentElectionService(json_service, congress_persons_by_departments, manage_congress_persons_by_department, 
                                                                                        build_congress, "proportionalDepartmental")    
    return proportional_department_election_service

def __get_json_service() -> ResultsElectionsPort: 
    json_files = JsonFiles()
    json_service = JsonResultsElection(json_files)
    return json_service